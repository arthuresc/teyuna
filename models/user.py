from sqlalchemy import Column, Integer, String
from database.base import Base, BaseMixins

class User(BaseMixins, Base):
  __tablename__="users"
  
  email = Column(String, unique=True, index=True, nullable=False)