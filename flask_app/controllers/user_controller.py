from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)


@app.route("/logout")
def logout():
    session["user_id"] = None
    return redirect("/")


@app.route("/register/user", methods=["POST"])
def register_user():
    users = User.get_all()

    if not User.validate_user(request.form, users):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "department": request.form["department"],
        "password": pw_hash,
    }

    user_id = User.save(data)

    session["user_id"] = user_id
    return redirect("/dashboard")

@app.route("/login/user", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password")
        return redirect("/")

    session["user_id"] = user_in_db.id
    return redirect("/dashboard")


@app.route("/user/account")
def edit_account():
    if not session.get("user_id"):
        flash("Please login to access the application")
        return redirect("/")
    else:
        user = User.get_by_id(session["user_id"])
        products = Product.get_all_products()
        return render_template("edit_user.html", user=user, products=products)


@app.route("/dashboard/edit/<int:user_id>/update", methods=["POST"])
def update_show(user_id):
    pass
