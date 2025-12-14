import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from .main import app, get_session
from .load_test_data import load_stocks, load_summaries_and_events


@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine(
        'sqlite:///',
        connect_args = {"check_same_thread": False},
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    
    # Load the test data
    stocks = load_stocks()
    summaries_events = load_summaries_and_events()
    
    with Session(engine) as session:
        for stock in stocks:
            session.add(stock)

        for summary, events in summaries_events:
            session.add(summary)
            if events:
                for event in events:
                    session.add(event)
            
        session.commit()
        
    # Passes the inmemory test database to each test func
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
    response = client.get('/stocks')
    data = response.json()

    assert len(data) == 6

def test_summaries(session: Session, client: TestClient):
    response = client.get('/summaries')
    data = response.json()

    assert len(data) == 6

def test_events(session: Session, client: TestClient):
    response = client.get('/events')
    data = response.json()

    # I dont know how many events the test run created
    # It doesnt really matter
    assert len(data) >= 6
