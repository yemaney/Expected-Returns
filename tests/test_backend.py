import pytest
from expected_returns.backend.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Expected Returns FastAPI Backend Root Landing Page"


def test_read_cape_country(client):
    response = client.post("/expected-returns/Country")
    assert response.status_code == 200
    assert [*response.json()] == ["date", "country", "cape"]


def test_read_cape_world(client):
    response = client.post("/expected-returns/World")
    assert response.status_code == 200
    assert [*response.json()] == ["cape", "date"]
