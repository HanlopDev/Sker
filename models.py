from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from database import Base

class UserBusinessOwner(Base):
    __tablename__ = "owner"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    business_name = Column(String, unique=True, index=True)
    location = Column(String, nullable=False)
    business_description = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password =Column(String, nullable=False)





