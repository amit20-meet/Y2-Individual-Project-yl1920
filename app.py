from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

#### Code here ######


@app.route('/' , methods=['GET', 'POST'])
def login_sign_up():
	global User_id
	'''	if request.method == 'POST':
		U = request.form['userName']
		P = request.form['password']
		User_id = sign_in(create_session(), U, P)
		if User_id == False:
			return render_template("login.html",)
		else:
			return render_template("home.html")
	if request.method == 'POST':
		Nick_name = request.form['Nick_Name']
		paswarde = request.form['password']
		Country = request.form['country']
		GAME_hours_day = request.form['Game_hour_day']
		sing_up(create_session(), Nick_name, paswarde, Country, GAME_hours_day)
		User_id = sign_in(create_session(), paswarde, Nick_name)
		Game_Name = request.form['Game_name']
		checkgame(create_session(), Game_Name, User_id)
		return render_template("home.html")'''
	return render_template("login.html")



@app.route('/login' , methods=['GET', 'POST'])
def login():
	global User_id
	if request.method == 'POST':
		U = request.form['userName']
		P = request.form['password']
		User_id = sign_in(create_session(), U, P)
		if User_id == False:
			return render_template("login.html")
		else:
			return redirect("/home")
	return render_template("login.html")



@app.route('/sign_up' , methods=['GET', 'POST'])
def sign_up():
	global User_id
	if request.method == 'POST':
		Nick_name = request.form['Nick_Name']
		paswarde = request.form['password']
		Country = request.form['country']
		GAME_hours_day = request.form['Game_hour_day']
		try:
			sing_up(create_session(), Nick_name, paswarde, Country, GAME_hours_day)
			print("sign up")
			User_id = sign_in(create_session(), U= Nick_name, P= paswarde)
			print(User_id)
			Game_name = request.form['Game_name']
			print("G_N")
			checkgame(create_session(), Game_name, User_id)
			return redirect("/home")
		except:
			print("excep")
			return render_template("login.html")	

	return render_template("login.html")


@app.route('/home', methods=['GET','POST'])
def home():

	'''t=query_all_profiles(create_session())
	h=query_all_massage_chat(create_session())
	g=query_all_Games(create_session())
	f=query_all_Fav(create_session())
	print(t)
	print(h)
	print(g)
	print(f)'''
	Suitable_profiles = []
	if request.method == 'POST':
		G = request.form['Game_name']
		Suitable_profiles = search(create_session(), G)

	return render_template("home.html", Suitable_profiles = Suitable_profiles)


	

@app.route('/change_info' ,  methods=['GET', 'POST'])
def change_info():
	global User_id 
	if request.method == 'POST':
		Nick_name = request.form['Nick_Name']
		paswarde = request.form['password']
		Country = request.form['country']
		GAME_hours_day = request.form['Game_hour_day']
		try:
			Game_name = request.form['Game_name']
			delete_game_fav (create_session(), User_id)
			checkgame(create_session(), Game_name, User_id)
			change_info(create_session(),User_id, Nick_name, Country, GAME_hours_day)
			return render_template("/home")
		except:
			change_info(create_session(),User_id, Nick_name, Country, GAME_hours_day)
			return render_template("/home")
	return render_template("change.html")



'''@app.route('/send_message')
def send_message():
	global User_id 
	print("work")
	massage_w = "Let's play"
	profile_that_send = User_id
	Profile_that_get = Suitable_profiles.User_id
	Send_massage(create_session(), massage_w, profile_that_send, Profile_that_get)
	return render_template("/home")'''


'''@app.route('/Chats')
def Chats():
	global User_id
	Chats =Chating(create_session(),User_id)

	return render_template("Chats.html", Chats)'''
#####################

if __name__ == '__main__':
	app.run(debug=True, threaded=False)