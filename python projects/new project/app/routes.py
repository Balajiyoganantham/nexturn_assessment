from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.model import User
from app import db  # Make sure to import db correctly

main = Blueprint('main', __name__)  # Corrected 'name' to '__name__'

@main.route('/')
def index():
    users = User.query.all()  # Query all users from the database
    return render_template('index.html', users=users)  # Render the index template

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('main.index'))  # Redirect to the index page

    return render_template('create.html')  # Render the create user form on GET request
@main.route('/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    if not user:
        flash('User not found')
        return redirect(url_for('main.index'))
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('main.index'))

