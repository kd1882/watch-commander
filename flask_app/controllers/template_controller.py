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
    
# getting started page
@app.route('/getting_started')
def getting_started():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        return render_template('getting_started.html')

# mgl_reference page
@app.route('/mgl_reference')
def mgl_reference():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('mgl_reference.html', user = user)

# role call notes page
@app.route('/role_call_notes')
def role_call_notes():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('rolecall_notes.html', user = user)

# dept info page
@app.route('/dept_info')
def dept_info():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('dept_information.html', user = user)

# legal page
@app.route('/legal')
def legal():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('legal.html', user = user)

# about page
@app.route('/about')
def about():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('about.html', user = user)

# faq page
@app.route('/faq')
def faq():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('faq.html', user = user)

# contact the devs page
@app.route('/contact')
def contact():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('contact.html', user = user)

# account management page
@app.route('/account_management')
def account_management():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('manage_account.html', user = user)

#  Logout success
@app.route('/logout/success')
def logout_success():
    return render_template('logout_success.html')