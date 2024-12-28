from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from confiig import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)  # Corrected: should be __name__ (double underscores)
    app.config.from_object(Config)
    
    db.init_app(app)  # Initialize the SQLAlchemy instance with the app

    from .routes import main as main_blueprint  # Ensure proper import
    app.register_blueprint(main_blueprint)  # Register the blueprint

    with app.app_context():  # Create an application context
        db.create_all()  # Create all tables

    return app  # Return the app instance
