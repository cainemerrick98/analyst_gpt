from typing import Annotated, Optional
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date

class Stocks(SQLModel, table=True):
    ticker: str = Field(primary_key=True)
    company: str
    tracked_sice: date

class Summaries(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    created: date
    ticker: str = Field(foreign_key='stock.ticker')
    title: str
    body: str
    sentiment: str

class KeyDates(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    date_: date
    ticker: str = Field(foreign_key='stock.ticker')
    title: str
    importance_for_price: str


sqlite_file_name = 'data/database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'


connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]




