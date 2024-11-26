from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    
    from .import routes
    routes.init__app(app)
    return app 