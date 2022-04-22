from  pydantic import BaseModel
from typing import Optional
from datetime import datetime
from  pydantic import BaseModel,HttpUrl,validator


















class Login(BaseModel):
    user_name : str
    password :  str 









class Token(BaseModel):
    access_token: str
    token_type: str




class TokenData(BaseModel):
    email: Optional[str] = None
 








class Person(BaseModel):
    id :int
    First_Name: str
    Last_Name: str
    Telephone_Number: int
    Email: str
    Password: str
    Blocked: bool
    Email_Verified: bool
    Created_At: Optional[datetime]
    Updated_At: Optional [datetime]
    class Config:
        orm_mode = True




