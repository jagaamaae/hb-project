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

class Country(db.Model):
    """A country aggregate."""

    __tablename__ = 'countries'

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    country= db.Column(db.String)

    def __repr__(self):
        return f'<Country country_id={self.country_id}'

class All_country(db.Model):
    """all countries time-series."""

    __tablename__ = 'all_countries'

    country_id = db.Column(db.Integer, autoincrement=True)
    date = db.Column(db.DateTime)
    confirmed = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    country= db.Column(db.String, primary_key=True)
    province_state=db.Column(db.String)

    reference=db.relationship("Reference")

    def __repr__(self):
        return f'<All_country country_id={self.country_id}'

class US(db.Model):

    __tablename__ = 'usa'

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    confirmed = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    country= db.Column(db.String)
    state=db.Column(db.String)

    def __repr__(self):
        return f'<US country_id={self.country_id}'


class Reference(db.Model):
    __tablename__ = 'references'

    reference_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    country= db.Column(db.String, db.ForeignKey('all_countries.country'),  unique=True )
    lat = db.Column(db.Integer)
    long = db.Column(db.Integer)
    population= db.Column(db.Integer)

    all_country=db.relationship("All_country")

    def __repr__(self):
        return f'<Reference reference_id={self.reference_id}>'


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

