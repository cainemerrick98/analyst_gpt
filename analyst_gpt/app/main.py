from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionDep, create_db_and_tables
from contextlib import asynccontextmanager
from sqlmodel import select, Session
from .return_models import Summary, KeyDate
from .database import Stocks, Summaries, KeyDates, engine
from .load_test_data import load_stocks, load_summaries_and_events


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    
    # Seed database
    with Session(engine) as session:
        if len(session.exec(select(Stocks)).all()) == 0:
            for stock in load_stocks():
                session.add(stock)

            for summary, events in load_summaries_and_events():
                session.add(summary)
                if events:
                    for event in events:
                        session.add(event)
            
            session.commit()

    yield

app = FastAPI(lifespan=lifespan)

origins = [
    'https://localhost'
]

CORSMiddleware(
    app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

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
    summaries = [Summary(company=result[1], **result[0].model_dump()) for result in session.exec(statement).all()]
    return summaries

@app.get('/events')
def events(session: SessionDep) -> list[KeyDate]:
    statement = select(KeyDates, Stocks.company).join(Stocks)
    events = [KeyDate(company=result[1], **result[0].model_dump()) for result in session.exec(statement).all()]
    return events