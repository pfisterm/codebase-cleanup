


print("CRYPTO REPORT...")


from app.utils import to_usd
from app.helper import get_crypto_data

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

tsd = get_crypto_data(symbol)

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
