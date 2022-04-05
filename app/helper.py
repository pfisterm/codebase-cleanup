import os
from dotenv import load_dotenv
import requests
import json
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def get_stock_data(symbol):
    """ 
    This function gets financial data from
    Alphavantage given a working API key 
    and a ticker symbol
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    return df

def get_crypto_data (symbol):
    """
    This function gets financial data from
    Alphavantage given a working API key 
    and a ticker symbol
    """
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Time Series (Digital Currency Daily)"]
    return tsd
