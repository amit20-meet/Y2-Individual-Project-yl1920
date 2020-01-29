from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_


def create_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def sing_up(session, Nick_name, paswarde, Country, GAME_hours_day):
	declarative_base = Profile(
		Nick_name=Nick_name,
		paswarde=paswarde, 
		Country=Country,
		GAME_hours_day=GAME_hours_day)
	session.add(declarative_base)
	session.commit()

def Send_massage(session, massage_w, profile_that_send, Profile_that_get):
	declarative_base = Massage(
		massage_w=massage_w,
		profile_that_send=profile_that_send,
		Profile_that_get=Profile_that_get)
	session.add(declarative_base)
	print("added")
	session.commit()


def change_info( session, User_id, Nick_name, Country, GAME_hours_day):
	declarative_base = session.query(
		Profile).filter_by(
		User_id=User_id).first()
	declarative_base.Nick_name = Nick_name
	declarative_base.Country = Country 
	declarative_base.GAME_hours_day = GAME_hours_day

def add_Game(session,Game_name):
	declarative_base = Game(
		Game_name = Game_name)
	session.add(declarative_base)
	session.commit()

def add_fev_game(session, User_Id_game, Game_Id_game):
	declarative_base = Profile_Game(
		User_Id_game = User_Id_game,
		Game_Id_game = Game_Id_game)
	session.add(declarative_base)
	print("added")
	session.commit()

def query_all_profiles(session):
	Profiles = session.query(
		Profile).all()
	return Profiles


def query_all_massage_chat(session):
	Chat = session.query(
		Massage).all()
	return Chat

def query_all_Games(session):
	Games = session.query(
		Game).all()
	return Games

def query_all_Fav(session):
	fav = session.query(
		Profile_Game).all()
	return fav

def Create_a_Chat(session):
	declarative_base = Chats_priv(
		personal_id = personal_id,
		Prof_id = Prof_id)
	session.add(declarative_base)
	print("added")
	session.commit()




def search(session, G):
	try:
		Game_name = G
		search_in_game=session.query(Game).filter_by(Game_name=Game_name).first()
		print("GAME NAME")
		print(search_in_game)
		try: 
			Game_Id_game=search_in_game.Game_id
			search_in_gameP= session.query(Profile_Game).filter_by(Game_Id_game=Game_Id_game).all()
			print(search_in_gameP)
			print("Profile_Game")
			try:
				search_in_P = []
				for p_g in search_in_gameP:
					User_id=p_g.User_Id_game
					search_in_P += session.query(Profile).filter_by(User_id=User_id).all()
					print(search_in_P)
				return search_in_P
			except:
				print("3")	
				search_in_P = []
				return search_in_P
		except:
			print("2")
			search_in_P = []
			return search_in_P
	except:
		print("1")
		search_in_P = []
		return search_in_P


def Chating (session, User_id):
	massage_U_S = session.query(Massage).filter_by(profile_that_send = User_id).all()
	id_sended = massage_U_S.Profile_that_get
	massage_U_G = session.query(Massage).filter_by(Profile_that_get = User_id).all()
	id_got = massage_U_G.profile_that_send
	Chats = session.query(Profile).filter(or_(User_id == id_got, User_id == id_sended)).all()
	return Chats

def sign_in(session, U, P):
	try:
		sing_U = session.query(Profile).filter_by(Nick_name = U, paswarde = P).first()
		return sing_U.User_id
	except: 
		return False

def checkgame(session, Game_name, User_id):
	print("pre-check")
	try:
		game = session.query(Game).filter_by(Game_name= Game_name).first()
		GG = game.Game_id
		User_Id_game = User_id
		Game_Id_game = GG
		print("try to add fev")
		add_fev_game(create_session(), User_Id_game, Game_Id_game)
	except:
		add_Game(create_session(), Game_name)
		GGG = session.query(Game).filter_by(Game_name = Game_name).first()
		G_id = GGG.Game_id
		User_Id_game = User_id
		Game_Id_game = G_id
		print("except to add fev")
		add_fev_game(create_session(), User_Id_game, Game_Id_game)

def delete_game_fav (session, User_id):
	 session.query(Profile_Game).filter_by(
	 User_Id_game=User_id).delete()
	 session.commit()


