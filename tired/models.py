import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
import datetime


Base = declarative_base()



class Person(Base):
     __tablename__ = 'everybody'
     id = Column(Integer, primary_key=True, index=True)
     First_Name = Column(String)
     Last_Name = Column(String)
     Email = Column(String)
     Password = Column (String)
     Telephone_Number = Column(Integer,primary_key=True, index = True)
     Blocked = Column(Boolean)
     Email_Verified = Column(Boolean)
     Created_At = Column(DateTime, default=datetime.datetime.now)
     Updated_At = Column(DateTime, default=datetime.datetime.now)
     


