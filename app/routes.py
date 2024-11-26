from flask import render_template

def init__app(app):
    @app.route('/')
    def index():
        return render_template('index.html')