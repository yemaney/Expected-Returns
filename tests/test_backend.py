from expected_returns.backend import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Expected Returns FastAPI Backend Root Landing Page"


def test_read_cape_country():
    response = client.get("/expected-returns/Country")
    assert response.status_code == 200
    assert [*response.json()] == [
        "Date",
        "Canada",
        "US",
        "UK",
        "Italy",
        "Spain",
        "Russia",
        "India",
        "Japan*",
        "China",
        "Hong Kong",
        "Australia",
    ]


def test_read_cape_world():
    response = client.get("/expected-returns/World")
    assert response.status_code == 200
    assert [*response.json()] == ["Global Stock Markets CAPE Ratio", "Date"]
