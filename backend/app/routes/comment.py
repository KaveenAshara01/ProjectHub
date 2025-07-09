from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.comment import Comment
from app.extensions import db

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/', methods=['POST'])
@jwt_required()
def add_comment():
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('task_id') and not data.get('project_id'):
        return jsonify({"msg": "Comment must be linked to either a task or a project"}), 400

    comment = Comment(
        text=data['text'],
        user_id=user_id,
        task_id=data.get('task_id'),
        project_id=data.get('project_id')
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201


@comment_bp.route('/task/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([c.to_dict() for c in comments])


@comment_bp.route('/project/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project_comments(project_id):
    comments = Comment.query.filter_by(project_id=project_id).all()
    return jsonify([c.to_dict() for c in comments])


@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"msg": "Comment deleted"})
