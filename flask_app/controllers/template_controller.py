from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')