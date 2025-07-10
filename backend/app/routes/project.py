from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.project import Project
from app.extensions import db
from app.utils.logger import log_activity

project_bp = Blueprint('project', __name__)

@project_bp.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_project = Project(
        title=data['title'],
        description=data.get('description'),
        user_id=int(user_id)
    )
    db.session.add(new_project)
    db.session.commit()
    log_activity(user_id, "create_project", f"User {user_id} created project '{new_project.title}'")
    return jsonify(new_project.to_dict()), 201


@project_bp.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    user_id = get_jwt_identity()
    projects = Project.query.filter_by(user_id=user_id).all()
    return jsonify([p.to_dict() for p in projects])


@project_bp.route('/projects/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())


@project_bp.route('/projects/<int:project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.title = data.get('title', project.title)
    project.description = data.get('description', project.description)
    db.session.commit()
    return jsonify(project.to_dict())


@project_bp.route('/projects/<int:project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"msg": "Project deleted"})
