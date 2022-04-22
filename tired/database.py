from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine("postgresql://postgres:postgres@:5432/postgres",
echo = True,
)





Base = declarative_base()
SessionLocal = sessionmaker(bind = engine)



def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()