import fastapi as fa
from fastapi.testclient import TestClient

from app import main


test_client = TestClient(main.app)

MULTIPLE_ELEMENTS = 2


def test_main():
    response = test_client.get("/")
    assert response.status_code == fa.status.HTTP_200_OK
    assert response.json() == "Hello world"


def test_get_skill_by_name():
    skill_name = "Python"
    test_client.post("/skills/", json={"name": "Python"})

    response = test_client.get(f"/skills/name/{skill_name}")
    assert response.status_code == fa.status.HTTP_200_OK
    assert response.json() == {"name": skill_name, "description": None}
