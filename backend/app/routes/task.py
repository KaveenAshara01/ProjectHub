from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.task import Task
from app.extensions import db
from app.utils.logger import log_activity
from app.models.project import Project

task_bp = Blueprint('task', __name__)

@task_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    project = Project.query.filter_by(id=data.get('project_id'), user_id=user_id).first()
    if not project:
        return jsonify({"msg": "Project not found or unauthorized"}), 404


    task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=data.get('due_date'),
        user_id=user_id,
        project_id=data['project_id']
    )
    db.session.add(task)
    db.session.commit()
    log_activity(user_id, "create_task", f"User {user_id} created task '{task.title}'")
    return jsonify(task.to_dict()), 201


@task_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([t.to_dict() for t in tasks])


@task_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())


@task_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.due_date = data.get('due_date', task.due_date)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return jsonify(task.to_dict())


@task_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"})
