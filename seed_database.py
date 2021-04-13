import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb covid19')
os.system('createdb covid19')
model.connect_to_db(server.app)
model.db.create_all()



# with open('data/us_simplified_json.json') as us:
#     us_data = json.loads(us.read())

# us_data_objects = []
# for data in us_data:
#     date, country, state, confirmed, deaths = (  
#                                     datetime.strptime(data['Date'], '%Y-%m-%d'), 
#                                     data["Country/Region"],
#                                     data['Province/State'],
#                                     data["Confirmed"], 
#                                     data['Deaths'] )

#     db_us= crud.create_us(date, country, state, confirmed, deaths)
#     us_data_objects.append(db_us)




with open('data/reference_json.json') as references:
    reference_data = json.loads(references.read())
reference_data_objects = []

for data in reference_data:
    country, lat, long, population = (
                                    data["Country_Region"],
                                    data["Lat"], 
                                    data["Long_"],
                                    data["Population"] )

    db_reference = crud.create_reference(
                                 country,
                                 lat, 
                                 long, 
                                 population)

    reference_data_objects.append(db_reference)

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





with open('data/time-series-19-covid-combined_json.json') as all_countries:
    all_country_data = json.loads(all_countries.read())

all_country_data_objects = []

for data in all_country_data:
    date, confirmed, recovered, deaths, country, province_state = (  
                                    datetime.strptime(data['Date'], '%Y-%m-%d'), 
                                    data["Confirmed"], 
                                    data["Recovered"],
                                    data['Deaths'], 
                                    data["Country"],
                                    data["Province/State"] )

    db_all_country = crud.create_all_country(date,
                                 confirmed,
                                 recovered, 
                                 deaths, 
                                 country,
                                 province_state)
    all_country_data_objects.append(db_all_country)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    user = crud.create_user(email, password)
