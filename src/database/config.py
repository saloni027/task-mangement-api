from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated

DB_URI = "postgresql://postgres:password@db:5432/postgres"

engine = create_engine(DB_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def init_db():
    Base.metadata.create_all(bind=engine)