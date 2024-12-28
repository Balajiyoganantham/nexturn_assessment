import os

class Config:
    SECRET_KEY = os.urandom(24)  # Generate a random secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/balaj/db/mydb.db'  # Adjust the path as needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save memory
