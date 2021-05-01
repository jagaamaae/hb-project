import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb covid')
os.system('createdb covid')
model.connect_to_db(server.app)
model.db.create_all()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    user = crud.create_user(email, password)

# with open('data/states.json') as states:
#     states_data=json.loads(states.read())
#     states_data_objects= []

#     for data in states_data:
#         state, population, capital = (
#                             data["state"],
#                             data["population"],
#                             data["capital_city"])
#         db_states = crud.create_states(state, 
#                                  population,  
#                                  capital)
#         states_data_objects.append(db_states)


# with open('data/us_confirmed_json.json') as us:
#     us_data = json.loads(us.read())

#     us_data_objects = []
#     for data in us_data:
#         date, country, county, state, confirmed = (  
#                                     datetime.strptime(data['Date'], '%Y-%m-%d'), 
#                                     data["Country/Region"],
#                                     data["Admin2"],
#                                     data["Province/State"],
#                                     data['Confirmed']
#                                      )

#         db_us = crud.create_us(date,
#                                  country,
#                                  county,
#                                  state,
#                                  confirmed)

#         us_data_objects.append(db_us)


with open('data/country_population.json') as references:
    reference_data = json.loads(references.read())
    reference_data_objects = []

    for data in reference_data:
        country,  population = (
                                    data["country"],
                                    data["population"] )

        db_reference = crud.create_reference(
                                 country, 
                                 population)

        reference_data_objects.append(db_reference)


with open('data/country_continent.json') as continent:
    continent_data = json.loads(continent.read())
    continent_data_objects = []

    for data in continent_data:
        country,  continent = (
                                    data["country"],
                                    data["continent"] )

        db_continent = crud.create_continent(
                                 country, 
                                 continent)

        continent_data_objects.append(db_continent)


with open('data/country_capital.json') as capital:
    capital_data = json.loads(capital.read())
    capital_data_objects = []

    for data in capital_data:
        country,  capital = (
                                    data["country"],
                                    data["city"] )

        db_capital = crud.create_capital(
                                 country, 
                                 capital)

        capital_data_objects.append(db_capital)




with open('data/countries-aggregated_json.json') as countries:
    country_data = json.loads(countries.read())

    country_data_objects = []
    for data in country_data:
        date, country, confirmed, recovered, deaths = (  
                                    datetime.strptime(data['Date'], '%Y-%m-%d'), 
                                    data["Country"],
                                    data["Confirmed"], 
                                    data["Recovered"],
                                    data['Deaths'] )

        db_country = crud.create_country(date,
                                 country,
                                 confirmed,
                                 recovered, 
                                 deaths)
        country_data_objects.append(db_country)


# with open('data/time-series-19-covid-combined_json.json') as all_countries:
#     all_country_data = json.loads(all_countries.read())

#     all_country_data_objects = []

#     for data in all_country_data:
#         date, confirmed, recovered, deaths, country, province_state = (  
#                                     datetime.strptime(data['Date'], '%Y-%m-%d'), 
#                                     data["Confirmed"], 
#                                     data["Recovered"],
#                                     data['Deaths'], 
#                                     data["Country/Region"],
#                                     data["Province/State"] )

#         db_all_country = crud.create_all_country(date,
#                                  confirmed,
                                 
#                                  recovered, 
#                                  deaths, 
#                                  country,
#                                  province_state)
                                 
#         all_country_data_objects.append(db_all_country)


