from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from random import choice

engine = create_engine('sqlite:////tmp/teste.db', echo=True)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(40))
    gold = Column(Integer)

    def __init__(self,id, username):
        self.id = id
        self.username = username

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
s = Session()