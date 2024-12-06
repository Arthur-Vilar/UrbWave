import os

BASE_DIR = os.path.abspath(os.path.dirname(_file_))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'UrbWave.db')}"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'UrbWave.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234')
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234')