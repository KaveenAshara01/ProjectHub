from app.routes.auth import auth_bp
# from app.routes.user import user_bp
from app.routes.project import project_bp
# from app.routes.task import task_bp
# from app.routes.comment import comment_bp
# from app.routes.activity import activity_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(project_bp, url_prefix='/api')
    # app.register_blueprint(task_bp, url_prefix='/api/tasks')
    # app.register_blueprint(comment_bp, url_prefix='/api/comments')
    # app.register_blueprint(activity_bp, url_prefix='/api/activities')
