from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, Date
from database import Base
from sqlalchemy.orm import relationship

class UserBusinessOwner(Base):
    __tablename__ = "owner"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    business_name = Column(String, unique=True, index=True)
    location = Column(String, nullable=False)
    business_description = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password =Column(String, nullable=False)

    items = relationship("Items",back_populates="owner")

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    id_owner = Column(Integer, ForeignKey("owner.id"))

    owner = relationship("UserBusinessOwner", back_populates="items")


