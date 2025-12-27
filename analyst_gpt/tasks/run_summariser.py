from .stock_summariser import summarise_stock_news
from app.database import Stocks, Summaries, KeyDates, engine, get_session
from sqlmodel import Session, select
import datetime as dt

def main():

    with Session(engine) as session:
        stocks = session.exec(select(Stocks)).all()

        for stock in stocks:
            print(stock)
            model_summary = summarise_stock_news(ticker=stock.ticker, company=stock.company)
            db_summary = Summaries(
                ticker=stock.ticker, created=dt.datetime.today().date(),
                title=model_summary.title, sentiment=model_summary.sentiment.value, body=model_summary.body,
                key_points="','".join([kp.text for kp in model_summary.key_points])
            )

            db_key_dates = [KeyDates(date_=kd.date_, ticker=stock.ticker, company=stock.company, title=kd.title, importance_for_price=kd.importance_for_price)
                            for kd in model_summary.key_dates] if model_summary.key_dates else None
            

            session.add(db_summary)

            if db_key_dates:
                for key_date in db_key_dates:
                    session.add(key_date)
        
        session.commit()
    


if __name__ == '__main__':
    main()