from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user.
    >>> user15= User(user_id = 15, email = joy@test.com, password = 123)
    >>> user15
    <user_id = 15, email = joy@test.com, password = 123>
    """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    

class Country(db.Model):
    __tablename__ = 'countries'
    country = db.Column(db.String, primary_key=True)
    population= db.Column(db.Integer)

    country_stats = db.relationship("CountryStats", backref='countries')
    # state_stats = db.relationship("USStates", backref='countries')
    
    def __repr__(self):
        return f'<Country country={self.country}>'

class CountryStats(db.Model):
    __tablename__ = 'country_stats'
    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True )
    date = db.Column(db.Date)
    country = db.Column(db.String, db.ForeignKey('countries.country'))
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    deaths = db.Column(db.Integer)    
   
    def __repr__(self):
        return f'<Country country={self.country}'

# class USStates(db.Model):

#     __tablename__ = 'us_states'

#     state_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     date = db.Column(db.DateTime)
#     country= db.Column(db.String, db.ForeignKey('countries.country'))
#     state=db.Column(db.String)
#     confirmed = db.Column(db.Integer)
#     deaths = db.Column(db.Integer)
  
#     def __repr__(self):
#         return f'<state state_id={self.state_id}'


def connect_to_db(flask_app, db_uri='postgresql:///covid', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)