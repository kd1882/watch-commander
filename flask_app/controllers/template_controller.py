from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

# landing page
@app.route('/')
def index():
    return render_template('login.html')

# Dashboard landing page
@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('dashboard.html', user = user)

#  Logout success
@app.route('/logout/success')
def logout_success():
    return render_template('logout_success.html')