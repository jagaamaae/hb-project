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
    
# test0@test.com | test
#  129 | 2020-05-29 | Afghanistan                      |     13662 |      1259 |    247
#  488 | 2020-03-10 | Albania                          |        10 |         0 |      0
# 2 | Albania                                      |    2866376

class Country(db.Model):
    __tablename__ = 'countries'
    country = db.Column(db.String, primary_key=True)
    population= db.Column(db.Integer)
    country_stats = db.relationship("CountryStats", backref='countries')
    
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

# class US(db.Model):

#     __tablename__ = 'usa'

#     country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     date = db.Column(db.DateTime)
#     country= db.Column(db.String)
#     state=db.Column(db.String)
#     confirmed = db.Column(db.Integer)
#     deaths = db.Column(db.Integer)
    
    

#     def __repr__(self):
#         return f'<US country_id={self.country_id}'


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
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

"""
covid_stats ----change the word "Stat/stats" to "stat/stats"
    covid_stats_id (pk) (autoincremtened)
    country_id (fk) (this comes from when you create the relationship)
    confirmed_count
    recovered_count
    deaths_count

    # relationships (these exist in sqlalchemy python but are NOT actual cols in the db):
    country = db.realtionship(*some syntax goes here*, backref="covid_stats") --this allows 
                        WAYS TO USE THE db.relationship to add the country_id to a stat row/record/sqlalchemy object
                                country_obj.covid_stats.append(aprl2)
                                stats_obj.country = country_obj
                                new_country_obj = Country(stat=stat_obj, name="some string".....all other fields)
                                new_stats_obj = CovidStat(date, )
                                one-to-many-relationship



Coutries
    country_id (pk)
    population
    lat
    long
    .... anything that describes the country, stats that don't change daily



# make new country obj:
us = Country(name="USA".....)
aprl2 = CovidStat(confirmed_count=10, recovered_count=10, deaths_count=10)

us.covid_stats.append(aprl2)
db.session.add(us)
db.session.commit()

"""