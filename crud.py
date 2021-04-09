from model import db, User, Reference, Country, All_country, US, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_reference(country_region, lat, long, population):

    reference= Reference(country_region=country_region, lat=lat, long=long, population = population)

    db.session.add(reference)
    db.session.commit()

    return reference

def create_country(date,country,confirmed,recovered, deaths):

    country = Country(date=date,
                                 country=country,
                                 confirmed=confirmed, 
                                 recovered=recovered,
                                 deaths=deaths)

    db.session.add(country)
    db.session.commit()

    return country

def get_user_email(email):
    user_email=User.query.filter_by(email=email).first()
    return user_email 

def get_user_by_email(email):
    user_email=User.query.filter_by(email=email).first()
    return user_email


if __name__ == '__main__':
    from server import app
    connect_to_db(app)