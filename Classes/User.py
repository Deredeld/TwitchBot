from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exists

from random import choice

import asyncio


engine = create_engine('sqlite:///C:\\Users\\noshea\\Pictures\\perso\\TwitchBot\\Database\\main.db')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
s = Session()





class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(40))
	gold = Column(Integer)


	def __init__(self,id, username):
		if self.userExists(id):
			self = s.query(User).get(id)
		else:
			self.id = id
			self.username = username
			s.add(self)
			s.commit()


	#Database
	def userExists(self,id):
		(ret, ), = s.query(exists().where(User.id==id))
		print("userExists:" + str(ret))
		return ret


#Mining
	def StartMine(self):
		loop = asyncio.get_event_loop()
		loop.call_later(5, self.stop)
		self.task = loop.create_task(self.mine())

		try:
		    loop.run_until_complete(self.task)
		except asyncio.CancelledError:
		    pass

	async def mine(self):
		while True:
			print("Mining...")
			await asyncio.sleep(1)


	#Stop async functions
	def stop(self):
		self.task.cancel()


Base.metadata.create_all()

