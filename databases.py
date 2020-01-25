from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def sing_up(session, Nick_name, , Country, GAME_hours_day):
	declarative_base = Profile(
		Nick_name=Nick_name,
		Country=Country,
		GAME_hours_day=GAME_hours_day)
	session.add(declarative_base)
	print("added")
	session.commit()

def Send_massage(session, id, massage_w, profile_that_send, Profile_that_get):
	declarative_base = Massage(
		id=id,
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

def add_fev_game(session, User_Id_game, Game_Id_game):
	declarative_base = Profile_Game(
		User_Id_game = User_Id_game,
		Game_Id_game = Game_Id_game)
	session.add(declarative_base)
	print("added")
	session.commit()

def query_all_profiles(session):
	products = session.query(
		Profile).all()
	return Profiles
def login(session, Nick_name
def query_all_massage_chat(session):
	Chat = session.query(
		Massage).all()
	return Chat

def query_last_massage_chat(session):
	last_massage = session.query(
		Massage).last()
	return last_massage

def search(session, x):
	search_in_game = session.query(Game).filter_by(Game_name = G).first()
	search_in_game.Game_Id
	search_in_gameP= session.query(Profile_Game).filter_by(Game_Id_game = search_in_game.Game_Id).all()
	search_in_gameP.Game_Id_game
	search_in_P = session.query(Profile).filter_by(User_id = search_in_gameP.Game_Id_game).all()
	return search_in_P.



