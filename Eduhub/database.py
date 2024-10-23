from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



URL="postgresql+psycopg2://postgres:postgres@localhost:5432/eduhub_db"

engine=create_engine(URL)


SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
 

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
       db.close()


