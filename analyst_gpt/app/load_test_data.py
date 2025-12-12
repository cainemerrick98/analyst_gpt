import pickle
from .return_models import Summary, KeyDate
from .database import Stocks
from datetime import datetime

def load_stocks() -> list[Stocks]:
    companies = [
        ('ASML', 'ASMLA'),
        ('Nvidia', 'NVDA'),
        ('Rolls-Royce', 'RR'),
        ('Vestas Wind', 'VWDRY'),
        ('Close Brothers Group', 'CBG'),
        ('NIO ADR', 'NIO')
    ]   

    stocks = []

    for company, ticker in companies:
        stocks.append(Stocks(ticker=ticker, company=company, tracked_sice=datetime.today()))
    
    return stocks
