from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import Enum


class Sentiment(Enum):
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'
    POSITIVE = 'positive'
    
class KeyDate(BaseModel):
    date_: date 
    title: str = Field(description='A short name of the event this key date represents')
    importance_for_price: str = Field(description='A short name of the event this key date represents')

class Summary(BaseModel):
    title: str = Field(description='A descriptive title for the summary')
    body: str
    key_dates = Optional[list[KeyDate]]
    sentiment: Sentiment = Field(description='The general or average sentiment across the articles reviewed')
    