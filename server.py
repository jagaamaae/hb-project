"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import Country, User, connect_to_db
import crud

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/countries')
def show_countries():
    countries = crud.get_countries()
    return render_template('all_countries.html', countries=countries)


@app.route('/countries/<country>')
def show_details(country):
    population=crud.get_population_by_country(country)
    cases=crud.get_country_cases(country)
    return render_template('country_details.html', cases = cases, population=population, country=country,)

@app.route('/users')
def show_users():
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<email>')
def show_users_details(email):
    user=crud.get_user_by_email(email)
    return render_template('user_details.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    print(user)
    if user:
        flash('This email/password combination is already taken. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_email(user_id)

    return render_template('user_details.html', user=user)

@app.route("/login-info", methods = ['POST'])
def login_info():
    email=request.form.get('email')
    password=request.form.get('password')
    user = crud.get_user_by_email(email)

    if user and user.password == password:
        flash('Logged in!') 
        session['email'] = user.email
        session['user_id'] = user.user_id
        return redirect('/')
    else:
        flash("Either email or password don't match")
    return redirect('/')

@app.route('/cases/<country>.json')
def data_dictionary(country):
    cases=crud.get_country_cases(country)
    data_dict={}
    for case in cases:
        data_dict[str(case.date)] = {
            "labels": [
            "date"
            "country",
            "confirmed",
            "recovered", 
            'deaths'
                ],
                "datasets": [
                    {"data": [case.date,case.country,case.confirmed, case.recovered, case.deaths],
                        "backgroundColor": [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56", 
                            "#FFCE56",
                            "#FFCE56"
                        ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56",
                            "#36A2EB",
                            "#36A2EB"
                        ]
                    }]
            }
    return jsonify(data_dict)


@app.route('/cases/<country>')
def melon_times_data():
    """Return time series data of Melon Sales."""

    data_dict = {
        "labels": ["January", "February", "March", "April", "May", "June", "July"],
        "datasets": [
            {
                "label": "Country",
                "fill": True,
                "lineTension": 0.5,
                "backgroundColor": "rgba(220,220,220,0.2)",
                "borderColor": "rgba(220,220,220,1)",
                "borderCapStyle": 'butt',
                "borderDash": [],
                "borderDashOffset": 0.0,
                "borderJoinStyle": 'miter',
                "pointBorderColor": "rgba(220,220,220,1)",
                "pointBackgroundColor": "#fff",
                "pointBorderWidth": 1,
                "pointHoverRadius": 5,
                "pointHoverBackgroundColor": "#fff",
                "pointHoverBorderColor": "rgba(220,220,220,1)",
                "pointHoverBorderWidth": 2,
                "pointRadius": 3,
                "pointHitRadius": 10,
                "data": [65, 59, 80, 81, 56, 55, 40],
                "spanGaps": False},
        ]
    }
    return data_dict
  
  
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
