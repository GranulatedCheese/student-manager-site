from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'student_manager'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    CORS(app)

    from .routes.student_r import student_bp
    app.register_blueprint(student_bp, url_prefix='/')

    from .models import Classroom, Student
    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')