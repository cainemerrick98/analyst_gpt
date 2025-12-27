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
    importance_for_price: str = Field(description='This should detail why this event will affect the price and in what direction it is likely to do so')

class KeyPoints(BaseModel):
    text: str

class Summary(BaseModel):
    title: str = Field(description='A descriptive title for the summary')
    body: str = Field(description='Use markdown formatting for body')
    key_dates: Optional[list[KeyDate]] = None
    sentiment: Sentiment = Field(description='The general or average sentiment across the articles reviewed')
    key_points: list[KeyPoints] = Field(description='1-3 key points to summarise findings')
    