from fastapi import status
from fastapi.testclient import TestClient

from app import dependencies, main
from app.config import test_database, database

database.Base.metadata.create_all(bind=test_database.engine)

db = test_database.TestLocalSession()


def override_get_db():
    try:
        yield db
    finally:
        db.close()


main.app.dependency_overrides[dependencies.get_db] = override_get_db

test_client = TestClient(main.app)


def test_main():
    response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello world"


def test_get_skills():
    response = test_client.get("/skills")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
