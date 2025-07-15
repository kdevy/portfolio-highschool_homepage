import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager, login_user
from app.models import db
from app.models.user_model import User
from app.views import user_bp
from app.views.user.static_page import static_page_bp

env_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_file_path)

def create_app(config=None):
    app = Flask(__name__)
    app.secret_key = "389e6d9681d0375b1de927d1e5f28871509ea42c11f1415053da686ad89b94f1"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{user}:{password}@{host}/{dbName}?charset=utf8".format(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASS'),
            host = os.getenv('DB_HOST'),
            dbName = os.getenv('DB_NAME')
        )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config:
        app.config.update(config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp)
    app.register_blueprint(static_page_bp)

    return app