from model import db, User, Stat, Country, connect_to_db 
# US,Country

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_reference(country, lat, long, population):

    reference= Country(country=country, lat=lat, long=long, population = population)

    db.session.add(reference)
    db.session.commit()

    return reference

# def create_country(date,country,confirmed,recovered, deaths):

#     country = Country(date=date,
#                                  country=country,
#                                  confirmed=confirmed, 
#                                  recovered=recovered,
#                                  deaths=deaths)

#     db.session.add(country)
#     db.session.commit()

#     return country

# def create_us(date, country, state, confirmed, deaths ):

#     us = US (date=date,
#                                  country=country,
#                                  state=state, 
#                                  confirmed=confirmed, 
#                                  deaths=deaths)

#     db.session.add(us)
#     db.session.commit()

#     return us


def create_all_country(date, confirmed, recovered, deaths, country, province_state):

    all_country = Stat(date=date,
                                 
                                 confirmed=confirmed, 
                                 recovered=recovered,
                                 deaths=deaths,
                                 country =country,
                                 province_state=province_state
                                 )

    db.session.add(all_country)
    db.session.commit()

    return all_country


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user


def get_countries():
    """Return all movies."""
    return Country.query.all()

def get_country_names(country_name):
    country_name = Country.query.get(country_name).first()
    return country_name

if __name__ == '__main__':
    from server import app
    connect_to_db(app)