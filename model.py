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

class CountryPopulation(db.Model):
    __tablename__ = 'country_population'
    country = db.Column(db.String, primary_key=True)
    population= db.Column(db.Integer)  
    country_capital_rel = db.relationship("CountryContinent", backref='country_population')
    country_continent_rel = db.relationship("CountryCapital", backref='country_population')
    country_stats_rel = db.relationship("CountryStats", backref='country_population')
    def __repr__(self):
        return f'<Country country={self.country}>'

class CountryContinent(db.Model):
    __tablename__ = 'country_continent'

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String, db.ForeignKey('country_population.country'))
    continent = db.Column(db. String)

    def __repr__(self):
        return f'<Country country={self.country}>'

class CountryCapital(db.Model):
    __tablename__ = 'country_capital'

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String, db.ForeignKey('country_population.country'))
    capital = db.Column(db. String)

    def __repr__(self):
        return f'<Country country={self.country}>'
  
class CountryStats(db.Model):
    __tablename__ = 'country_stats'
    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True )
    date = db.Column(db.Date)
    country = db.Column(db.String, db.ForeignKey('country_population.country'))
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    deaths = db.Column(db.Integer)    
   
    def __repr__(self):
        return f'<Country country={self.country}'


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