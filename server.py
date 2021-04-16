"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import Country, User, connect_to_db
import crud
# Replace this with routes and view functions!

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
    distinct_countries = set()
    display_countries = []
    for country in countries:
        if country.country not in distinct_countries:
            display_countries.append(country)
            distinct_countries.add(country.country)
    
    
    return render_template('all_countries.html', display_countries=display_countries)

@app.route('/countries/<country_name>')
def show_details(country_name):
    country=crud.get_country_by_name(country_name)
    return render_template('country_details.html', country=country)

# @app.route('/all_cases')
# def show_details(cases):
#     return render_template('all_cases.html', country=cases)


@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    print(user)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_email(user_id)

    return render_template('user_details.html', user=user)


# @app.route('/users/<email>')
# def show_users_details(email):
#     user=crud.get_user_by_email(email)
#     return render_template('user_details.html', user=user)
#     # return redirect ('countries')

# @app.route("/users", methods = ["POST"])
# def register_user():
#     email=request.form.get('email')
#     password=request.form.get('password')

#     user = crud.get_user_by_email(email)
#     if user:
#         flash('You already have an account')
    
#     else:
#         crud.create_user(email, password)
#         flash('Account created! Please log in.')

#     return redirect('/')
    
@app.route("/login-info", methods = ['POST'])
def login_info():
    email=request.form.get('email')
    password=request.form.get('password')
    user = crud.get_user_by_email(email)

    if user and user.password == password:
        flash('Logged in!') 
        session['email'] = user.email
        session['user_id'] = user.user_id
        return redirect(f'users/{email}')
    else:
        flash("Either email or password don't match")
    return redirect('/')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)