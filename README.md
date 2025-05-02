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
  # 📚 Student Performance Dashboard

This project visualizes student academic data to uncover trends, performance gaps, and dropout risks using Tableau and Google Sheets.

## 📌 Tools Used
- Google Sheets
- Tableau
- Python (for preprocessing)

## 🎯 Dashboard Features
- Attendance vs Performance analysis
- Grade distribution by subject and batch
- Dropout risk alert panel

## 🧪 Dataset
Anonymized student data containing:
- Subject scores
- Attendance records
- Assignment submissions

## 🚀 How to Use
1. Run `preprocess.py` to clean and enrich the dataset
2. Import the cleaned CSV into Tableau
3. Build filters: class, subject, grade level

## 📊 Sample Dashboard
![Dashboard](dashboards/performance_dashboard.png)

4. Update DB credentials in `etl_pipeline.py`
5. Run: `python scripts/etl_pipeline.py`

## 📁 Output
- Stored 100K+ records in PostgreSQL
- Visualized trends like top gainers, volatility, and sector performance

