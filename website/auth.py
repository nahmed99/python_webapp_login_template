from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


# Define authorisation routes

# login route can handle both get and post requests.
# get request is when the login url is accessed.
# post request is when the login button is pressed on the login page.
@auth.route('/login', methods=['GET', 'POST'])
def login():
   data = request.form
   print(data)
   return render_template("login.html", boolean=False)


@auth.route('/logout')
def logout():
   return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
   return render_template("sign_up.html")
