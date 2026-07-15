from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.sql import func

Base = declarative_base()

class BaseMixins():
    id = Column(Integer, primary_key=True, index=True)
    
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    updated_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)

from models.user import User
from models.product import Product