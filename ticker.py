from tradingview_ta import TA_Handler
import pandas as pd
import pandas_ta as ta
import binance.client
from binance.client import Client


Pkey = ""
Skey = ""
client = Client(api_key=Pkey, api_secret=Skey)


tickers = ["ACHUSDT", "BTCUSDT", "VETUSDT"]
intervals = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d", "1W", "1M"]


def my_function(ticker, interval):
    try:

        data = TA_Handler(symbol=ticker, screener="crypto",
                          exchange="binance", interval=interval)
        if data.get_analysis() is not None:
            ticker = data.get_analysis().symbol
            interval = data.get_analysis().interval
            time = data.get_analysis().time
            global_detail = data.get_analysis().summary
            global_detail1 = data.get_analysis().moving_averages
            global_detal2 = data.get_analysis().indicators
            print(interval, ":", "\n", "oscillators :",
                  global_detail['RECOMMENDATION'], "\nMOVING AVERAGES :", global_detail1['RECOMMENDATION'], "\n")
    except Exception as e:
        print(e)


for ticker in tickers:
    print(ticker, ":")
    print('----------------------')
    price = client.get_avg_price(symbol=ticker)
    print("price : ", price['price'])
    for interval in intervals:
        my_function(ticker, interval)

    print('-----------------------------------------')
