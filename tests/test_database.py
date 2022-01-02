import pytest
from expected_returns.database.main import app, get_session
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool


@pytest.fixture(name="session")  #
def session_fixture():  #

    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  #
def client_fixture(session: Session):  #
    def get_session_override():  #
        return session

    app.dependency_overrides[get_session] = get_session_override  #
    client = TestClient(app)  #

    yield client  #
    app.dependency_overrides.clear()


def test_update_database_World(client: TestClient):

    response = client.post("/World", json={"cape": {0: 3.5}, "date": {0: "2022/01/01"}})
    app.dependency_overrides.clear()
    # data = response.json()

    assert response.status_code == 200
    assert response.json()["Message"] == "Completed update of World table in database!"


def test_update_database_Country(client: TestClient):

    response = client.post(
        "/Country",
        json={"cape": {0: 3.5}, "date": {0: "2022/01/01"}, "country": {0: "Canada"}},
    )
    app.dependency_overrides.clear()
    # data = response.json()

    assert response.status_code == 200
    assert (
        response.json()["Message"] == "Completed update of Country table in database!"
    )
