import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_seeder import FlaskSeeder


def create_app():
    app = Flask(__name__)
    load_dotenv()

    CORS(app, origins=[f"http://127.0.0.1:3000", "http://localhost:3000", os.getenv('DOMAIN')],
         supports_credentials=True)

    if os.getenv('ENV') == "develop":
        app.config.update(
            SESSION_COOKIE_SAMESITE='None',
            SESSION_COOKIE_SECURE='False'
        )

    init_database(app)
    init_bcrypt(app)
    init_seeder(app)
    init_login_manager(app)
    init_principle(app)
    init_blueprints(app)

    return app


def init_database(app: Flask):
    from .database import db_init
    db_init(app)


def init_bcrypt(app: Flask):
    from .bcrypt import bcrypt_init
    bcrypt_init(app)


def init_login_manager(app: Flask):
    from .login_manager import login_manager_init
    login_manager_init(app)


def init_principle(app: Flask):
    from .principle import principle_init
    principle_init(app)


def init_seeder(app: Flask):
    from .database import db
    seeder = FlaskSeeder()
    seeder.init_app(app, db)


def init_blueprints(app: Flask):
    prefix = '/api'
    from adapters.auth_bp import auth_blueprint
    from adapters.student_bp import student_blueprint
    from adapters.class_bp import class_blueprint
    app.register_blueprint(auth_blueprint, url_prefix=prefix)
    app.register_blueprint(student_blueprint, url_prefix=prefix)
    app.register_blueprint(class_blueprint, url_prefix=prefix)