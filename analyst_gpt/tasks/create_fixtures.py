from .stock_summariser import summarise_stock_news

companies = [
    ('ASML', 'ASMLA'),
    ('Nvidia', 'NVDA'),
    ('Rolls-Royce', 'RR'),
    ('Vestas Wind', 'VWDRY'),
    ('Close Brothers Group', 'CBG'),
    ('NIO ADR', 'NIO'),
    ('NuScale PowerCorp', 'SMR')
]

if __name__ == '__main__':

    for company, ticker in companies:
        print(company)
        summary = summarise_stock_news(ticker, company)
        with open(f'./app/test_data/{company}.json', 'w') as f:
            f.write(summary.model_dump_json())

