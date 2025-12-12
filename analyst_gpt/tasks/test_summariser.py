import pytest
from .stock_summariser import summarise_stock_news
from .models import Summary 

def save_summary(summary: Summary, name: str):

    with open(f'./summaries/{name}.md', 'w') as f:
        f.write(summary.title)
        f.write('\n\n')
        f.write(f'sentiment: {summary.sentiment}')
        f.write('\n\n')
        f.write(summary.body)
        f.write('\n\n')
        f.write('Key Dates\n\n')
        if summary.key_dates:
            f.writelines([f'- {kd.title} - {kd.date_}: {kd.importance_for_price}\n' for kd in summary.key_dates])


def test_summarise_apple():
    ticker = 'AAPL'
    company = 'Apple'

    summary = summarise_stock_news(ticker, company)

    save_summary(summary, 'apple')

    
