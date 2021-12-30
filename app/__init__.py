from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_smorest import Api, Blueprint, abort
from flask_migrate import Migrate, migrate

""" Extensions """
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
sm = Api()
mg = Migrate()


def create_app():
    load_dotenv(".env")
    app = Flask(__name__)
    set_config(app)
    register_extensions(app)
    register_blueprint()
    return app


def register_blueprint():
    from .auth import auth_bp
    sm.register_blueprint(auth_bp)


def set_config(app: Flask):
    env_keys = [
        "PROD", "SQLALCHEMY_DATABASE_URI",
        "SECRET_KEY", "JWT_SECRET_KEY"
    ]

    for env_key in env_keys:
        app.config[env_key] = environ.get(env_key)

    app.config["API_TITLE"] = "API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)


def register_extensions(app: Flask):
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    sm.init_app(app)
    mg.init_app(app, db)
