from fastapi import APIRouter, Depends
from schemas import ItemCreate
from sqlalchemy.orm import Session
from hashing import Hasher
from models import Items
from datetime import datetime
from database import get_db

router = APIRouter()

@router.post("/items", tags=["items"])
def item_create(item: ItemCreate, db:Session=Depends(get_db)):
    date_posted = datetime.now().date()
    id_owner = 1
    item = Items(**item.dict(), date_posted=date_posted, id_owner=id_owner)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

