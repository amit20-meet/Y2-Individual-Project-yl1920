from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Profile(Base):
	__tablename__ = 'Profiles'
	User_id = Column(Integer, primary_key=True)
	Nick_name = Column(String, unique=True)
	paswarde = Column(String, unique=True)
	Country = Column(String)
	GAME_hours_day = Column(String) 



class Massage(Base):
	__tablename__ = 'Chat'
	massage_id= Column(Integer,primary_key=True)#hour fof sending
	massage_w = Column(String)#what wroten in the massage
	profile_that_send = Column(String)#who send the massage
	Profile_that_get = Column(String)# who got the massage (needed?????????????????????????)

class Game(Base):
	__tablename__ = 'games'
	Game_id=Column(Integer, primary_key=True)
	Game_name=Column(String, unique=True)

class Profile_Game(Base):
	__tablename__ = 'All'
	User_Id_game=Column(Integer)
	Game_Id_game= Column(Integer)
		
		
