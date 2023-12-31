from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.mgl_model import MGL
from flask_app.static.utils.format_helpers import *

bcrypt = Bcrypt(app)

# landing page
@app.route('/')
def index():
    ma_depts = ma_dept_tuple
    return render_template('login.html', ma_depts = ma_depts)

# Dashboard landing page
@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('dashboard.html', user = user)
    
# Mental Health resources page
@app.route('/mental_health_resources')
def getting_started():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        return render_template('mental_health_reference.html')

# mgl_reference page
@app.route('/mgl_reference')
def mgl_reference():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('mgl_reference.html', user = user)
    
@app.route('/mgl_reference/chapter/<string:chapter_id>')
def mgl_reference_chapter(chapter_id):
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        sections = MGL.get_sections(chapter_id)
        print(sections)
        return render_template('mgl_chapter.html', user = user, mgl_reference_chapter = sections)
    
@app.route('/mgl_reference/chapter/section')
def mgl_reference_section():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('mgl_section.html', user = user)

# oui reference page
@app.route('/oui_reference')
def role_call_notes():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('oui_reference.html', user = user)

# dept info page
@app.route('/dv_resources')
def dept_info():
    if not session.get('user_id'):
        flash("Please login to access the application")
        return redirect('/')
    else:
        user = User.get_by_id(session['user_id'])
        return render_template('domestic_resources.html', user = user)

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