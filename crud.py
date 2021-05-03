from model import CountryCapital, db, User,  CountryPopulation,  CountryContinent,  CountryStats,  connect_to_db 


"""CRUD operations."""



def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# def create_states(state, population, capital):
#     state = USInfo(state=state, population=population, capital=capital)

#     db.session.add(state)
#     db.session.commit()

#     return state


# def create_us(date, country, county, state, confirmed):

#     us = USStates (date=date,
#                                  country=country,
#                                  county=county,
#                                  state=state, 
#                                  confirmed=confirmed)

#     db.session.add(us)
#     db.session.commit()

#     return us


def create_reference(country,  population):

    reference= CountryPopulation(country=country, population = population)

    db.session.add(reference)
    db.session.commit()

    return reference

def create_capital(country,  capital):

    capital= CountryCapital(country=country, capital=capital)

    db.session.add(capital)
    db.session.commit()

    return capital

def create_continent(country,  continent):

    continent= CountryContinent(country=country, continent=continent)

    db.session.add(continent)
    db.session.commit()

    return continent


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
    """Return all countries."""
    return CountryPopulation.query.all()

def get_country_cases(country):
    cases = CountryStats.query.filter(CountryStats.country==country).all()
    return cases

def get_country_info(country):
    population = CountryPopulation.query.filter(CountryPopulation.country == country).first().population
    capital = CountryCapital.query.filter(CountryCapital.country==country).first().capital
    continent = CountryContinent.query.filter(CountryContinent.country ==country).first().continent
    return population, capital, continent

def get_continent(country):
    north_america = CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent == "North America").first()
    south_america = CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent == "South America").first()
    europe= CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent == "Europe").first()
    asia= CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent == "Asia").first()
    oceania = CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent =="Oceania").first()
    africa = CountryContinent.query.filter_by(country=country).filter(CountryContinent.continent == "Africa").first()
    return north_america, europe, asia, south_america, oceania, africa

if __name__ == '__main__':
    from server import app
    connect_to_db(app)



