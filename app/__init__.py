from flask import Flask
from config import Config
def creat_app():
    app = Flask (__nome__)
    from.import routes
    routes.init_app(app)
    return app 