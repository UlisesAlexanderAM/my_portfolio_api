import fastapi as fa
from fastapi.testclient import TestClient

from app import main
from app.data import dependencies
from app.database import database, databate_test


def override_get_db():
    """Override the get_db dependency to use the test database.

    Yields:
        An open database session
    """
    try:
        yield db
    finally:
        db.close()


main.app.dependency_overrides[dependencies.get_db] = override_get_db

test_client = TestClient(main.app)

MULTIPLE_ELEMENTS = 2


def test_main():
    response = test_client.get("/")
    assert response.status_code == fa.status.HTTP_200_OK
    assert response.json() == "Hello world"


def test_get_zero_skills():
    response = test_client.get("/skills")
    assert response.status_code == fa.status.HTTP_200_OK
    assert response.json() == []


def test_add_skill():
    response = test_client.post("/skills", json={"name": "Python"})
    assert response.status_code == fa.status.HTTP_201_CREATED


def test_get_skill_by_name():
    skill_name = "Python"
    test_client.post("/skills/", json={"name": "Python"})

    response = test_client.get(f"/skills/name/{skill_name}")
    assert response.status_code == fa.status.HTTP_200_OK
    assert response.json() == {"name": skill_name}


def test_get_one_skill():
    test_client.post("/skills", json={"name": "Python"})
    response = test_client.get("/skills")
    assert response.status_code == fa.status.HTTP_200_OK
    assert len(response.json()) == 1


def test_get_two_skills():
    test_client.post("/skills", json={"name": "Python"})
    test_client.post("/skills", json={"name": "Java"})

    response = test_client.get("/skills")
    assert response.status_code == fa.status.HTTP_200_OK
    assert len(response.json()) == MULTIPLE_ELEMENTS
