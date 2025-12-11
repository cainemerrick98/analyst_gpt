import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from .main import app, get_session


@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine(
        'sqlite:///'
    )
    #TODO add fixture data
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name='client')
def client_fixture(session: Session):
    def get_session_override():
        return session 
    
    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_root(session: Session, client: TestClient):
    response = client.get('/')
    data = response.json()

    assert data['message'] == 'Hello World'

def test_stocks(session: Session, client: TestClient):
    ...

def test_summaries(session: Session, client: TestClient):
    ...

def test_events(session: Session, client: TestClient):
    ...
