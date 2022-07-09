from fastapi import APIRouter, Depends
from schemas import BusinesOwnerCreate
from database import get_db
from sqlalchemy.orm import Session
from hashing import Hasher
from models import UserBusinessOwner

router = APIRouter()

@router.get("/businessowner", tags=["users"])
def get_users():
    return {"data": "hello users"}

@router.post("/businessowner", tags=["users"])
def get_user(user: BusinesOwnerCreate, db:Session=Depends(get_db)):
    user = UserBusinessOwner(
            username=user.username,
            business_name=user.business_name,
            location = user.location,
            business_description = user.business_description,
            email = user.email,
            password = Hasher.get_hash_password(user.password)
            )
    db.add(user)
    db.commit()
    db.flush(user)
    return db

