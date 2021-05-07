I'm a former international relations specialist and polyglot turned to public policy analyst and economist. 

Start with a joke. How can an economist express their love? Via chart!

Hence, my project is all about charts.
My project helps economist to load data and 
A)quickly gets a chart  from a given json, CSV
B)also gives basic facts about different countries
C)sorts countries into continents so that economists can quickly grab their data

Tools:Flask, jinja, javascript, jquery, ajax, sqlalchemy, cookies and sessions, postgresql

Star features: Charts JS, buttons (a)changes the words depending whether user is in session b) has a form and post request c) nav bar's user interface that is very easy to use.

About backend: I'm using postgres sql databse covid which has a connection with 3 other tables(population, capital, continent) using the common variable of a country name. Also, there is a user's table called users, which generates 10 dummy users and stores additional users.

I'm seeding all these databases from the json file that I have it locally.

At last, I have another python file that has sqlalchemy functions which allow me to query the tables and pull certain countries based on their continent. Additinally, I'm pulling my covid case data through get_country_cases function, which will feed into my chars. At last, the users function is important for getting users by their email or as an entier object. All of this is being added and being commited to my database.

Overall, I have 16 html files, which show data that was pulled from the functions of crud.py

About front end:
 the base.html is inherited throughout all of my other hmtl files. The nav bar is very user-friendly, because you can see all of my routes.

 The star of the show is my login/logout button which is responsive and changes teh wording when teh user is in session. I used JS AJAX request by using fetch built-in function.
 
 Here I'm showing my jinja codes, which were used throughout all of my html.

 I'm showing my Account button, which has a pop-up where Form action is present and does a post request. 

 Here is my settings dropdown menu, which personlizes teh experience by providing the user information about their profile.

 Also, flash messages throughout.

 Lastly, I showed my JS files: charts, login JS ajax request, and selection of countries JS ajax request. 

On the website, I'm logging in and showing my flash messages. 

Once, logged in I can go and select the country of my choice, which creates an ajax request and has a link, where I click and shows my charts. 

Another star of the website is the collapsible button, which I created using JS and CSS tools.