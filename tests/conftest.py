
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.database.config import Base, get_db
from main import app
from decouple import config

TEST_DB_URI = config("TEST_DB_URI")

engine = create_engine(TEST_DB_URI, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)

    # Override the dependency
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    # Drop the tables after the test run
    Base.metadata.drop_all(bind=engine)










