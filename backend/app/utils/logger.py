from app.extensions import db
from app.models.activity import Activity

def log_activity(user_id, action_type, description):
    activity = Activity(
        user_id=user_id,
        action_type=action_type,
        description=description
    )
    db.session.add(activity)
    db.session.commit()
