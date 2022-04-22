from fastapi import APIRouter,Depends,HTTPException, status
import schema,models,database
from sqlalchemy.orm import Session
from . import hashing, token,oauth2
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/api/authentication',tags = ['login'])
async def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
      user =db.query(models.Person).filter(models.Person.Email == request.username).first()
      if not user:
           raise HTTPException(status_code = 404, detail='request not possible, invalid credentials')
    

      if not hashing.hash.verify(user.Password,request.password):
           raise HTTPException(status_code = 404, detail='request not possible, incorrect password ')





     
      access_token = token.create_access_token(data={"sub": user.Email},)
      return {"access_token": access_token, "token_type": "bearer"}





    





