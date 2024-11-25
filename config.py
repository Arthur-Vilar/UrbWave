import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///UrbWave.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'