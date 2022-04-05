

print("STOCKS REPORT...")

from app.utils import to_usd
from app.helper import get_stock_data

symbol = input("Please input a ticker symbol (default: 'NFLX'): ") or "NFLX"

df = get_stock_data(symbol)
latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
