from fastapi import FastAPI
from .database import SessionDep, create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.get('/summaries')
def summaries(session: SessionDep):
    return {'summaries':[]}

@app.get('/events')
def events(session: SessionDep):
    return {'events':[]}