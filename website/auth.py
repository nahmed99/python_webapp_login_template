from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


# Define authorisation routes

# login route can handle both get and post requests.
# get request is when the login url is accessed.
# post request is when the login button is pressed on the login page.
@auth.route('/login', methods=['GET', 'POST'])
def login():
   return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
   return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

   # POST request
   if request.method == 'POST':
      email = request.form.get('email')
      firstName = request.form.get('firstName')
      password1 = request.form.get('password-1')
      password2 = request.form.get('password-2')

      if len(email) < 4:
         flash('Email must be greater than 3 characters.', category='error')
      elif len(firstName) < 2:
         flash('First name must be greater than 1 character.', category='error')
      elif len(password1) < 7:
         flash('Password must be at least 7 characters.', category='error')
      elif password1 != password2:
         flash('Passwords don\'t match.', category='error')
      else:
         # add user to the database (switch statement currently don't exist in Python - will do in version 10!)
         flash('Account created.', category='success')


   return render_template("sign_up.html")
