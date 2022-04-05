

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv

from app.utils import to_usd

from app.helper import get_stock_data

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a ticker symbol (default: 'NFLX'): ") or "NFLX"

url = get_stock_data(ALPHAVANTAGE_API_KEY, symbol)

df = read_csv(url)
#print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
