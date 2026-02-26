import yfinance as yf
import os

def fetch_data(ticker: str, start_date: str):
    data = yf.download(ticker, start=start_date,auto_adjust=False)
    #os.makedirs("Data/Raw_data", exist_ok=True)
    data.to_csv(f"Data/Raw_data/{ticker}_daily.csv")
    return data

if __name__ == "__main__":
    fetch_data("AAPL", "2016-01-01")

