import sqlite3
from authlib.integrations.flask_client import OAuth
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from datetime import timedelta
from sqlalchemy.exc import IntegrityError,DataError,DatabaseError,InterfaceError,InvalidRequestError
from werkzeug.routing import BuildError
from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash
from flask_login import UserMixin,login_user,LoginManager,current_user,logout_user,login_required
from werkzeug.utils import secure_filename
import os
from app import create_app,db,login_manager,bcrypt
from models import User
from forms import login_form,register_form
import crud
from models import User, Car


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()



@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('list'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )



# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data

            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        
    return render_template("auth.html",
        

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/auth')
def main_route():
    return render_template("profile.html")

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        
            return redirect(url_for('list'))

    return render_template('createpage.html')

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    #return redirect(url_for('static', filename='uploads/' + filename), code=301)




@app.route('/cart/<int:id>')
def add_to_cart(id):
    return redirect(url_for('main_route'))



@login_required
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id, ):
    car = get_car(id)

    if request.method == 'POST':
        
            return redirect(url_for('list'))

    return render_template('edit.html', car=car)


def get_db_connection():
    conn = sqlite3.connect('instance/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/<int:id>/delete/', methods=('POST', 'GET'))
def delete(id):


@app.route('/')
def list():  # put application's code here
    
    return render_template('cars.html', cars=cars)



@app.route('/<int:id>/desc', methods=('POST', 'GET'))
def description(id):
    car = get_car(id)

    return render_template('description.html', car=car)


if __name__ == "__main__":
    app.run(debug=True)
