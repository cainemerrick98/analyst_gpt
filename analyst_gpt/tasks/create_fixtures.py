from .stock_summariser import summarise_stock_news
import pickle

companies = [
    ('ASML', 'ASMLA'),
    ('Nvidia', 'NVDA'),
    ('Rolls-Royce', 'RR'),
    ('Vestas Wind', 'VWDRY'),
    ('Close Brothers Group', 'CBG'),
    ('NIO ADR', 'NIO')
]

if __name__ == '__main__':

    for company, ticker in companies:
        print(company)
        summary = summarise_stock_news(ticker, company)
        with open(f'../app/test_data/{company}.pkl', 'wb') as f:
            f.write(pickle.dumps(summary))

