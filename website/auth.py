from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


# Define authorisation routes

# login route can handle both get and post requests.
# get request is when the login url is accessed.
# post request is when the login button is pressed on the login page.
@auth.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      # get the data passed in from the login form
      email = request.form.get('email')
      password = request.for.get('password')

      # query the database - verify that email address already exists 

   return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
   return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

   # POST request
   if request.method == 'POST':
      # get the data passed in from the sign-up form
      email = request.form.get('email')
      firstName = request.form.get('firstName')
      password_1 = request.form.get('password-1')
      password_2 = request.form.get('password-2')

      if len(email) < 4:
         flash('Email must be greater than 3 characters.', category='error')
      elif len(firstName) < 2:
         flash('First name must be greater than 1 character.', category='error')
      elif len(password_1) < 7:
         flash('Password must be at least 7 characters.', category='error')
      elif password_1 != password_2:
         flash('Passwords don\'t match.', category='error')
      else:
         # db_variable/column = models_variable
         new_user = User(email=email, first_name=firstName, password=generate_password_hash(password_1, method='sha256'))

         # add user to the database (switch statement currently don't exist in Python - will do in version 10!)
         db.session.add(new_user)
         db.session.commit()

         flash('Account created.', category='success')

         # redirect the user to their homepage
         return redirect(url_for('views.home'))


   return render_template("sign_up.html")
