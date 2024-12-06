from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(_name_)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main
    app.register_blueprint(main)
    return app