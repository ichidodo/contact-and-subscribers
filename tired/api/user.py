from typing import List
from fastapi import APIRouter,Depends,HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import schema,models,database 
from . import hashing,oauth2
from sqlalchemy.orm import Session




router = APIRouter()




db = database.SessionLocal







@router.post('/api/user/',response_model = schema.Person,status_code = status.HTTP_201_CREATED, tags=['user'])
async def user(request:schema.Person,db:Session = Depends(database.get_db)):
    new_user = models.Person(id = request.id,First_Name = request.First_Name, Last_Name = request.Last_Name,Email = request.Email,Telephone_Number = request.Telephone_Number,Password = hashing.hash.becrypt(request.Password),Blocked = request.Blocked,Email_Verified = request.Email_Verified,Created_At = request.Created_At,Updated_At = request.Updated_At)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
   




