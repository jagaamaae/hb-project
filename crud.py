from model import db, User,  Country, CountryStats, connect_to_db 
# US,Country

"""CRUD operations."""

"""CRUD operations."""

from model import db, User, CountryStats, Country, connect_to_db 

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_reference(country,  population):

    reference= Country(country=country, population = population)

    db.session.add(reference)
    db.session.commit()

    return reference

def create_country(date,country,confirmed,recovered, deaths):

    country = CountryStats(date=date,
                                 country=country,
                                 confirmed=confirmed, 
                                 recovered=recovered,
                                 deaths=deaths)

    db.session.add(country)
    db.session.commit()

    return country


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()


def get_countries():
    """Return all movies."""
    return Country.query.all()

def get_population_by_country(country):
    population = Country.query.filter(Country.country == country).first().population
    return population

def get_country_cases(country):
    cases = CountryStats.query.filter(CountryStats.country==country).all()
    return cases

if __name__ == '__main__':
    from server import app
    connect_to_db(app)




# def create_us(date, country, state, confirmed, deaths ):

#     us = US (date=date,
#                                  country=country,
#                                  state=state, 
#                                  confirmed=confirmed, 
#                                  deaths=deaths)

#     db.session.add(us)
#     db.session.commit()

#     return us

# def create_all_country(date, confirmed, recovered, deaths, country, province_state):

#     all_country = Stat(date=date,
                                 
#                                  confirmed=confirmed, 
#                                  recovered=recovered,
#                                  deaths=deaths,
#                                  country =country,
#                                  province_state=province_state
#                                  )

#     db.session.add(all_country)
#     db.session.commit()

#     return all_country
# def create_all_country(date, confirmed, recovered, deaths, country, province_state):

#     all_country = Stat(date=date,
                                 
#                                  confirmed=confirmed, 
#                                  recovered=recovered,
#                                  deaths=deaths,
#                                  country =country,
#                                  province_state=province_state
#                                  )

#     db.session.add(all_country)
#     db.session.commit()

#     return all_country
