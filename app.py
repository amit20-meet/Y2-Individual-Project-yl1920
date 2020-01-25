from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

#### Code here ######



@app.route('/')
def home():
	return render_template("home.html")
e_info():
	if request.m
@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['userName'] != 'gever' or request.form['password'] != 'gever123':
			error = 'Please try again.'
			return render_template("home.html")
		else:
			return render_template("change.html" )
	else:
		return render_template('login.html', error=error)

@app.route('/change' ,  methods=['GET', 'POST'])
def change_info():
	if request.method == 'POST':
		Nick_name =request.form["Nick name"]
		Favorite_games = request.form["games that you love to play"]
		Country = request.form["Country"]
		GAME_hours_day = request.form["time of the day that ou play"]
	change_info(create_session(),Nick_name, Favorite_games, Country, GAME_hours_day)
	return render_template("change.html")



#####################

if __name__ == '__main__':
	app.run(debug=True)