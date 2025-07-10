from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.activity import Activity

activity_bp = Blueprint('activity', __name__)

@activity_bp.route('/', methods=['GET'])
@jwt_required()
def get_activity_logs():
    user_id = get_jwt_identity()
    logs = Activity.query.filter_by(user_id=user_id).order_by(Activity.timestamp.desc()).all()
    return jsonify([a.to_dict() for a in logs])
