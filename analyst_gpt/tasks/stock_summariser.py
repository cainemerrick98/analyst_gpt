from openai import OpenAI
from .models import Summary
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_KEY')

prompt = """
System / Assistant persona:
You are an analyst that produces concise, factual weekly news summaries about public companies. Use web_search to gather primary news sources and produce a structured Summary object that matches the JSON/Pydantic schema provided to the API via response_format.

User prompt:
Produce a weekly news summary for the company below using web_search to collect news from the PAST 7 DAYS.

Company:
- Ticker: {ticker}
- Name: {company}

Tool usage rules:
1. MUST call web_search (at least once) before producing the final Summary.
2. Use queries combining company name + ticker + terms like: "news", "press release",
   "earnings", "guidance", "regulatory", "product", "layoffs", "SEC filing", "market reaction".
3. You may make additional web_search calls to follow up or disambiguate results.
4. Do not produce the final JSON until you have processed search results and verified dates.

Content & quality rules (high-level):
- Prefer primary sources (press releases, filings, reputable outlets).
- For dates use ISO format YYYY-MM-DD.
- Avoid hallucinated facts; if uncertain, cite the source in the evidence step (see below).

Output constraints (final message only):
- The final message MUST be the JSON object that exactly matches the schema supplied via response_format (Summary with title, body, key_dates, sentiment).
- Do NOT include any explanatory text outside that JSON object.
- Key dates should ONLY be future dates

Example Body:

**Rolls-Royce Announces £200 Million Share Buyback Program**

On December 18, 2025, Rolls-Royce announced an interim share buyback program of up to £200 million, following the completion of a £1 billion buyback in November. The new program is set to commence on January 2, 2026, and conclude by February 24, 2026, ahead of the company's full-year 2025 results scheduled for February 26, 2026. UBS AG London Branch will manage the buyback, with shares purchased intended for cancellation to reduce share capital. ([ts2.tech](https://ts2.tech/en/rolls-royce-rr-l-stock-news-today-200m-buyback-analyst-targets-and-2026-catalysts-dec-18-2025/?utm_source=openai))

**Analyst Updates on Rolls-Royce Holdings**

Deutsche Bank Aktiengesellschaft raised its price target for Rolls-Royce Holdings plc from GBX 1,000 to GBX 1,220, indicating a potential upside of 12.13% from the stock's previous close. The stock currently holds a consensus rating of "Moderate Buy," with four analysts issuing buy ratings and one hold rating. ([marketbeat.com](https://www.marketbeat.com/instant-alerts/deutsche-bank-aktiengesellschaft-issues-positive-forecast-for-rolls-royce-holdings-plc-lonrr-stock-price-2025-08-07/?utm_source=openai))

Additionally, Berenberg upgraded Rolls-Royce from a 'Sell' to a 'Hold' rating, citing expectations of improved fleet dynamics through 2035 and ongoing operational improvements within the group. The upgrade reflects a potential shift in market sentiment towards the aerospace and defense giant. ([asktraders.com](https://www.asktraders.com/analysis/rolls-royce-stock-shifts-to-neutral-as-berenberg-cites-favorable-fleet-dynamics/?utm_source=openai))
"""


llm = OpenAI(api_key=api_key)

def summarise_stock_news(ticker: str, company: str) -> Summary:
    company_prompt = prompt.format(ticker=ticker, company=company)
    return llm.responses.parse(
        model='gpt-4.1',
        tools=[{ "type": "web_search_preview" }],
        input=company_prompt,
        text_format=Summary
    ).output_parsed