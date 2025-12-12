from fastapi import FastAPI
from .database import SessionDep, create_db_and_tables
from contextlib import asynccontextmanager
from sqlmodel import select
from .return_models import Summary, KeyDate
from .database import Stocks, Summaries, KeyDates, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.get('/stocks')
def stocks(session: SessionDep) -> list[Stocks]:
    statement = select(Stocks)
    stocks = session.exec(statement).all()
    return stocks

@app.get('/summaries')
def summaries(session: SessionDep) -> list[Summary]:
    statement = select(Summaries, Stocks.company).join(Stocks)
    summaries = session.exec(statement).all()
    return summaries

@app.get('/events')
def events(session: SessionDep) -> list[KeyDate]:
    statement = select(KeyDates, Stocks.company).join(Stocks)
    events = session.exec(statement).all()
    return events