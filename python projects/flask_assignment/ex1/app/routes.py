from flask import Blueprint, render_template

# Create a blueprint for employee routes
employee_routes = Blueprint('employee_routes', __name__)

# Define an index route
@employee_routes.route('/')
def index():
    return render_template('index.html')


