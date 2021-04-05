from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'jur821jd39dsfgh sdfj' # In PRODUCTION, this needs to be kept secret!!! At the moment it is just some random (secret!) value.

   # The database will be stored in the same location as the __init__.py file:
   app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
   db.init_app(app) # the app that we will use with this database

   # import blueprints
   from .views import views
   from .auth import auth
   
   # register blureprints (home urls) with flask app
   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')

   return app
