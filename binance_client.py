import binance.client
from binance.client import Client


Pkey = ""
Skey = ""
client = Client(api_key=Pkey, api_secret=Skey)


tickers = ["ACHUSDT", "BTCUSDT", "VETUSDT"]


def i():
    for ticker in tickers:
        price = client.get_avg_price(symbol=ticker)
        print(price['price'])
