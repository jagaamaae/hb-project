"""Server for covid cases app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import User, Country, CountryStats, connect_to_db
import crud
import json

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Show homepage with form for user's name. If name already stored, redirect."""
    if 'email' in session:
        return redirect('/countries')
    return render_template('homepage.html')

@app.route('/countries')
def show_countries():
    countries = crud.get_countries()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template('all_countries.html', countries=countries, flags=flags)

@app.route('/get-email')
def get_user():
    user = request.args.get("email")
    session['email']= user
    return redirect("/countries")

@app.route('/countries/<country>')
def show_details(country):
    population=crud.get_population_by_country(country)
    cases=crud.get_country_cases(country)
    # if 'email' not in session:
    #     return redirect('/')
    return render_template('country_details.html', cases = cases, population=population, country=country,)

@app.route('/users')
def show_users():
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<email>')
def show_users_details(email):
    user=crud.get_user_by_email(email)
    return render_template('user_details.html', user=user)

@app.route("/users", methods = ["POST"])
def register_user():
    email=request.form.get('email')
    password=request.form.get('password')
    user = crud.get_user_by_email(email)
    if user:
        flash('The account exists already. Try another account')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')
    
@app.route("/login-info", methods = ['POST'])
def login_info():
    email=request.form.get('email')
    password=request.form.get('password')
    user = crud.get_user_by_email(email)

    if user and user.password == password:
        flash('Logged in!') 
        session['email'] = user.email
        session['user_id'] = user.user_id
        return redirect('/countries')
    else:
        flash("Either email or password don't match")
    return redirect('/')

  
@app.route("/logout", methods=['POST'])
def logout_info():
    if 'email' in session:
        session.clear()
    return redirect('/')


@app.route('/countries/<country>.json')
def data_dictionary(country):
    cases=crud.get_country_cases(country)
    data_dict={}
    confirmed =[case.confirmed for case in cases]
    recovered=[case.recovered for case in cases]
    deaths=[case.deaths for case in cases]
    dates=[str(case.date) for case in cases]
    data_dict = {
                "labels": dates,
                 "datasets": 
                     [{"label":"confirmed",
                     "data": confirmed,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                             
                     }, 
                     {"label":"recovered",
                     "data": recovered,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                              
                     }, 
                     {"label":"deaths",
                     "data": deaths,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                               
                     }
                 
                     ]
             }
    return jsonify(data_dict)


@app.route('/countries/<country>.json')
def data_countries(country):
    cases=crud.get_country_cases(country)
    data_dict={}
    confirmed =[case.confirmed for case in cases]
    recovered=[case.recovered for case in cases]
    deaths=[case.deaths for case in cases]
    dates=[str(case.date) for case in cases]
    data_dict = {
                "labels": dates,
                 "datasets": 
                     [{"label":"confirmed",
                     "data": confirmed,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                             
                     }, 
                     {"label":"recovered",
                     "data": recovered,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                              
                     }, 
                     {"label":"deaths",
                     "data": deaths,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                               
                     }
                 
                     ]
             }
    return jsonify(data_dict)



@app.route('/most_affected/<country>.json')
def data_most_affected(country):
    cases=crud.get_country_cases(country)
    data_dict={}
    confirmed =[case.confirmed for case in cases]
    recovered=[case.recovered for case in cases]
    deaths=[case.deaths for case in cases]
    dates=[str(case.date) for case in cases]
    data_dict = {
                "labels": dates,
                 "datasets": 
                     [{"label":"confirmed",
                     "data": confirmed,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                             
                     }, 
                     {"label":"recovered",
                     "data": recovered,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                              
                     }, 
                     {"label":"deaths",
                     "data": deaths,
                         "borderColor": "rgba(220,220,220,0.2)",
                        
                        "hoverBackgroundColor": 
                            "#FFF"
                               
                     }
                 
                     ]
             }
    return jsonify(data_dict)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)