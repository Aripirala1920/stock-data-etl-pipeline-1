# stock-data-etl-pipeline-1
# 📈 Stock Data ETL Pipeline

This project extracts stock data for Nifty 100 companies using Python, transforms it, and loads it into PostgreSQL for analysis and visualization in Tableau.

## 💻 Tech Stack
- Python, Pandas, SQLAlchemy
- PostgreSQL
- Tableau
- yfinance API

## 📊 Dashboard Preview
![Dashboard](dashboards/stock_dashboard.png)

## 🚀 How to Run
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Update DB credentials in `etl_pipeline.py`
4. Run: `python scripts/etl_pipeline.py`

## 📁 Output
- Stored 100K+ records in PostgreSQL
- Visualized trends like top gainers, volatility, and sector performance

