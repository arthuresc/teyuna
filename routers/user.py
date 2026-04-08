from sqlalchemy import Column, Integer, String
from database.base import base

class User(Base):
  __tablename__="users"
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, uniquyye=True, index=True, nullable=False)