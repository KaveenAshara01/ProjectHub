from flask import Flask
from app.extensions import db, migrate, jwt, cors
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, supports_credentials=True)

    register_blueprints(app)

    return app
