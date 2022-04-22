import uvicorn
import fastapi
import passlib
from passlib.context import CryptContext
import bcrypt
import schema,models,database
from api import user, authentication
from fastapi import FastAPI,Depends
from fastapi import File,UploadFile,FastAPI
from PIL import Image
import secrets
import shutil
from typing import List
from database import Base,engine
from sqlalchemy.orm import Session
from api import authentication,user,token,oauth2,hashing

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def index():
    return {'message':'Hello Unyime'}




 
@app.post("/")
async def upload_profile_pic(file: UploadFile = File(...)):
    with open(f"{file.filename}","wb")as buffer:
        shutil.copyfileobj(file.file,buffer)
    return{"file_name":file.filename}

@app.put("/")
async def update_profile_pic(file: UploadFile = File(...)):
    with open(f"{file.filename}","wb")as buffer:
        shutil.copyfileobj(file.file,buffer)
    return{"file_name":file.filename}





@app.post("/img")
async def multiple_documents_upload(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f"{file.filename}","wb")as buffer:
            shutil.copyfileobj(img.file,buffer)
    return{"file_name":"files uploaded"}




@app.get("/")
async def logout():
    return index()






























def configure():
    configure_routing()



def configure_routing():
    
    app.include_router(user.router)
    app.include_router(authentication.router)
    
    
if __name__ == '__main__':
    configure()
    uvicorn.run(app, host = '127.0.0.1',port = 8000)

else:
    configure()











