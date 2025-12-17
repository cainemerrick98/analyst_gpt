import json
from .database import Stocks, Summaries, KeyDates
import datetime as dt

companies = {
    'ASML':'ASMLA',
    'Nvidia':'NVDA',
    'Rolls-Royce':'RR',
    'Vestas Wind':'VWDRY',
    'Close Brothers Group':'CBG',
    'NIO ADR':'NIO'
}

def load_stocks() -> list[Stocks]:
    stocks = []

    for company, ticker in companies.items():
        stocks.append(Stocks(ticker=ticker, company=company, tracked_sice=dt.datetime.today()))
    
    return stocks


def load_summaries_and_events() -> list[tuple[Summaries, KeyDates]]:
    parsed_model_outputs = []
    for company, ticker in companies.items():
        with open(f'./app/test_data/{company}.json', 'r') as f:
            model_output = json.loads(f.read())

        summary = Summaries(
            ticker=ticker, company=company, created=dt.datetime.today().date(),
            title=model_output['title'], body=model_output['body'], sentiment=model_output['sentiment']
        )
        key_dates = [KeyDates(date_=dt.datetime.strptime(kd['date_'], '%Y-%m-%d'), ticker=ticker, company=company, title=kd['title'], importance_for_price=kd['importance_for_price'])
                     for kd in model_output['key_dates']] if model_output['key_dates'] else None
        parsed_model_outputs.append(
            (summary, key_dates)
        )

    return parsed_model_outputs