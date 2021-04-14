from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

# class Country(db.Model):
#     """A country aggregate."""

#     __tablename__ = 'countries'

#     country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     date = db.Column(db.DateTime)
#     confirmed = db.Column(db.Integer)
#     recovered = db.Column(db.Integer)
#     deaths = db.Column(db.Integer)
#     country= db.Column(db.String)

#     def __repr__(self):
#         return f'<Country country_id={self.country_id}'

class AllCountry(db.Model):
    """all countries time-series."""

    __tablename__ = 'all_countries'


    stat_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    country= db.Column(db.String)
    province_state=db.Column(db.String)

    reference=db.relationship("Reference")

    def __repr__(self):
        return f'<AllCountry country_id={self.country_id}'


class Reference(db.Model):
    __tablename__ = 'references'


    reference_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    stat_id = db.Column(db.Integer, db.ForeignKey('all_countries.stat_id'),  unique=True )
    lat = db.Column(db.Integer)
    long = db.Column(db.Integer)
    population= db.Column(db.Integer)

    all_country=db.relationship("AllCountry")

    def __repr__(self):
        return f'<Reference reference_id={self.reference_id}>'


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


def connect_to_db(flask_app, db_uri='postgresql:///covid19', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

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