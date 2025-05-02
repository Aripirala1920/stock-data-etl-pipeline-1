import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Database connection (adjust as needed)
engine = create_engine('postgresql://username:password@localhost:5432/stockdb')

# List of Nifty 100 symbols (sample)
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']

def fetch_stock_data(ticker):
    df = yf.download(ticker, period="1mo", interval="1d")
    df['Ticker'] = ticker
    return df.reset_index()

all_data = pd.concat([fetch_stock_data(t) for t in tickers], ignore_index=True)

# Save to CSV (optional)
all_data.to_csv("data/sample_stocks.csv", index=False)

# Load into PostgreSQL
all_data.to_sql("nifty_stock_data", engine, if_exists="replace", index=False)

print("ETL Pipeline completed.")
