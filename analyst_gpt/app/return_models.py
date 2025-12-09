from pydantic import BaseModel
from datetime import date

"""
These are the models that will be returned by the api
"""

class Summary(BaseModel):
    ticker: str
    company: str
    created: date
    title: str
    body: str
    sentiment: str

class KeyDate(BaseModel):
    date_: date
    ticker: str
    company: str
    title: str
    importance_for_price: str
