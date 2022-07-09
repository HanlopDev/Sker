from fastapi import FastAPI
from config import setting
from routers import businessowner
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

tags = [
        {
            "name": "users",
            "description": "user route"
            },
        {
            "name": "items",
            "description": "item route"
            },

        ]

app = FastAPI(
        title = setting.TITLE,
        description = setting.DESCRIPTION,
        version = setting.VERSION,
        contact = {
            "name": setting.NAME,
            "email": setting.EMAIL},
        openapi_tags = tags 
        )

app.include_router(businessowner.router)

