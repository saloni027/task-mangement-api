
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.database.config import Base, get_db
from main import app
from decouple import config
from src.auth.auth_utilities import create_access_token

TEST_DB_URI = config("TEST_DB_URI")

engine = create_engine(TEST_DB_URI, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def pytest_collection_modifyitems(config, items):
    # Move tests marked with `run_last` to the end of the test execution order
    last_tests = [item for item in items if 'run_last' in item.keywords]
    other_tests = [item for item in items if 'run_last' not in item.keywords]
    items[:] = other_tests + last_tests


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="package")
def client():
    Base.metadata.create_all(bind=engine)

    # Override the dependency
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    #Drop the tables after the test run
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="package")
def auth_token():
    token = create_access_token(data={"sub": 'user1'})
    return token











