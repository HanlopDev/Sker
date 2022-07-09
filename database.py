from sqlalchemy import create_engine 
from config import setting 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

SQLALCHEMY_DATABASE_URL = setting.POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    try:
        db = Sessionlocal()
        yield db

    finally:
        db.close()
