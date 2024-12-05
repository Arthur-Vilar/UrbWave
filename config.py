import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///UrbWave.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False