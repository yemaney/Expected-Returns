from expected_returns.backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Expected Returns FastAPI Backend Root Landing Page"


def test_read_cape_country():
    response = client.post("/expected-returns/Country")
    assert response.status_code == 200
    assert [*response.json()] == ["Date", "Nation", "value"]


def test_read_cape_world():
    response = client.post("/expected-returns/World")
    assert response.status_code == 200
    assert [*response.json()] == ["Global Stock Markets CAPE Ratio", "Date"]
