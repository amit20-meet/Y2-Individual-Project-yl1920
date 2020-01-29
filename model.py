from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Profile(Base):
	__tablename__ = 'Profiles'
	User_id = Column(Integer, primary_key=True)
	Nick_name = Column(String, unique=True)
	paswarde = Column(String)
	Country = Column(String)
	GAME_hours_day = Column(String)

	def __repr__(self): 
		list1 = [self.User_id, self.Nick_name, self.paswarde, self.Country, self.GAME_hours_day ]
		return str(list1)

class Chats_priv(Base):
	__tablename__ = 'CCHATS'
	Chat_id = Column(Integer, primary_key= True)
	personal_id = Column(Integer)
	Prof_id = Column(Integer)


class Massage(Base):
	__tablename__ = 'Chat'
	massage_id= Column(Integer,primary_key=True)#hour fof sending
	massage_w = Column(String)#what wroten in the massage
	profile_that_send = Column(String)#who send the massage
	Profile_that_get = Column(String)# who got the massage (needed?????????????????????????)

	def __repr__(self): 
		list1 = [self.massage_id, self.massage_w, self.profile_that_send, self.Profile_that_get]
		return str(list1)

class Game(Base):
	__tablename__ = 'games'
	Game_id=Column(Integer, primary_key=True)
	Game_name=Column(String)


	def __repr__(self): 
		list1 = [self.Game_id, self.Game_name]
		return str(list1)

class Profile_Game(Base):
	__tablename__ = 'All'
	prof_id = Column(Integer, primary_key= True)
	User_Id_game=Column(Integer)
	Game_Id_game= Column(Integer)

	def __repr__(self): 
		list1 = [self.prof_id, self.User_Id_game, self.Game_Id_game]
		return str(list1)
		
		
