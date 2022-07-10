from  pydantic import BaseModel, EmailStr

class BusinesOwnerCreate(BaseModel):
    username : str
    business_name : str
    location : str
    business_description : str
    email : EmailStr
    password : str

class ItemCreate(BaseModel):
    title : str
    description : str

