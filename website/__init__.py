from flask import Flask

def create_app():
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'jur821jd39dsfgh sdfj' # In PRODUCTION, this needs to be kept secret!!! At the moment it is just some random (secret!) value.

   # import blueprints
   from .views import views
   from .auth import auth
   
   # register blureprints (home urls) with flask app
   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')

   return app
