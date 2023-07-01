from fastapi import status
from fastapi.testclient import TestClient

from app import dependencies, main
from app.config import database, test_database

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


def test_add_skill():
    response = test_client.post("/skills", json={"name": "Python", "level": "0.5"})
    assert response.status_code == status.HTTP_201_CREATED


def test_get_skill_by_name():
    skill_name = "Python"
    test_client.post("/skills", json={"name": "Python", "level": "0.5"})

    response = test_client.get(f"/skills/{skill_name}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": skill_name, "level": 0.5, "id": 1}
