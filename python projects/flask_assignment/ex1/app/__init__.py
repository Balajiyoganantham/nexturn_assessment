from flask import Flask
from .routes import employee_routes

def create_app():
    app = Flask(__name__)


    app.register_blueprint(employee_routes)

    return app
