import pytest
from .stock_summariser import summarise_stock_news
from .models import Summary 

def save_summary(summary: Summary, name: str):

    with open(f'./summaries/{name}.txt', 'w') as f:
        ...

def test_summarise_apple():
    ticker = 'AAPL'
    company_name = 'Apple'

    summary = summarise_stock_news(ticker, company_name)

    
