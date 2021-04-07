from . import db  # import the 'variable' db from any file in current folder
from flask_login import UserMixin
from sqlalchemy.sql import func


# The class name has upper case first letter, the datanase will 
# use a lower case first letter for the table name.

class Note(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   data = db.Column(db.String(10000))
   date = db.Column(db.DateTime(timezone=True), default=func.now())
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # foreign key is the 'id' from 'user' table



# UserMixin is only used for this table
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(150), unique=True)
   password = db.Column(db.String(150))
   first_name = db.Column(db.String(150))
   notes = db.relationship('Note')  # link to the notes on the 'note' table. BEWARE: upper case first letter in table name here (SQLAlchemy work this way)!!!