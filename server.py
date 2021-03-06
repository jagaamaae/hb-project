"""Server for covid cases app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import CountryContinent, User, CountryPopulation, CountryStats, connect_to_db
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
    return render_template("homepage.html")

@app.route('/europe')
def show_eu():
    countries = crud.get_europe()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template('Europe.html', countries=countries, flags=flags)

@app.route('/asia')
def show_asia():
    countries = crud.get_asia()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template("Asia.html", countries=countries, flags=flags)

@app.route('/north_america')
def show_noth_america(): 
    countries = crud.get_north_america()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template("North_America.html", countries=countries, flags=flags)

@app.route('/africa')
def show_africa():
    countries = crud.get_africa()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template("Africa.html", countries=countries, flags=flags)

@app.route('/oceania')
def show_oceania():
    countries = crud.get_oceania()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template("Oceania.html", countries=countries, flags=flags)

@app.route('/countries')
def show_countries():
    countries = crud.get_countries()
    with open('./data/reversed.json','r') as f:
        flags = json.loads(f.read())
        flags=flags[0]
    return render_template('all_countries.html', countries=countries, flags=flags)

@app.route('/countries/<country>')
def show_details(country):
    population=crud.get_country_population(country)
    cases=crud.get_country_cases(country)
    return render_template('country_details.html', cases = cases, population=population, country=country)

@app.route('/select')
def show_selector():
    countries = crud.get_countries()
    return render_template('index.html', countries=countries)

@app.route('/most_affected_details/<country>')
def get_details(country):
    population = crud.get_country_population(country.lstrip())

    return jsonify({'country': country, 'population': population})

    # return redirect(f'/countries/{country.lstrip()}')

@app.route("/contact")
def show_contact():
    return render_template("/contact.html")

@app.route("/about")
def show_about():
    return render_template("/about.html")
   
@app.route('/get-email')
def get_user():
    user = request.args.get("email")
    session['email']= user
    return redirect("/countries")

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
    
    with open('./data/countries-aggregated_json.json','r') as f:
        country_data = json.loads(f.read())
        country_data = country_data[0]


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

@app.route('/logged-in')
def is_logged_in():
    
    return jsonify({'data': session.get('email')})




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)