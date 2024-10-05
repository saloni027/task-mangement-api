from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated
from decouple import config

# Database URI loaded from environment variables
DB_URI = config("DB_URI")

engine = create_engine(DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session for a request.

    Yields:
        Session: A SQLAlchemy session instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


async def init_db():
    """
    Initialize the database by creating all tables.

    This function creates all tables defined in the Base metadata 
    if they do not already exist.
    """
    Base.metadata.create_all(bind=engine)
