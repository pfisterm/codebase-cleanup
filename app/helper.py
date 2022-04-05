def get_stock_data(ALPHAVANTAGE_API_KEY, symbol):
    """ 
    This function gets financial data from
    Alphavantage given a working API key 
    and a ticker symbol
    """
    return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

def get_crypto_data (ALPHAVANTAGE_API_KEY, symbol):
    """
    This function gets financial data from
    Alphavantage given a working API key 
    and a ticker symbol
    """
    return f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
