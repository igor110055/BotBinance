import get_data as gd
from tradingview_ta import TA_Handler
import pandas as pd
import pandas_ta as ta
import binance.client
from binance.client import Client


Pkey = ""
Skey = ""
client = Client(api_key=Pkey, api_secret=Skey)

#tickers = ["BTCUSDT","RLCUSDT"]
##################
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 2000)

Pkey = ''
Skey = ''

client = Client(api_key=Pkey, api_secret=Skey)


def vwap(df, period):
    klines = df
    klines["tP"] = ta.hlc3(high=klines["High"],
                           low=klines["Low"], close=klines["Close"])
    klines["tPV"] = klines["tP"] * klines["Volume"]
    klines["mTPV"] = ta.sma(klines["tPV"], length=period)
    klines["mV"] = ta.sma(klines["Volume"], length=period)
    klines["vwap"] = klines["mTPV"] / klines["mV"]
    vwap = klines["vwap"]
    columns = klines.columns
    for i in range(6, len(columns)):
        del klines[columns[i]]
    return vwap


#Tickers =  ['BTCUSDT', 'ETHUSDT', 'NEOUSDT']
def VwapPercent(ticker, interval, peroid):
    data = gd.get_klines(ticker, interval, "1400 hours ago UTC+1")
    vwapp = vwap(data, peroid)
    LastOneVwap = vwapp.iloc[-1]
    klines = client.get_avg_price(symbol=ticker)
    klines = float(klines['price'])

    return (klines-LastOneVwap)/klines*100


tickers = ["XRPBTC", "POWRUSDT"]
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
            global_detal2 = data.get_analysis().oscillators
            print("╔", interval, ":", "\n", "Summary :",
                  global_detail['RECOMMENDATION'], "\nMOVING AVERAGES :", global_detail1['RECOMMENDATION'], "\n", "oscillators :", global_detal2['RECOMMENDATION'], "╝")
    except Exception as e:
        print(e)


for ticker in tickers:
    print("     →", ticker, "←")
    print('----------------------')
    price = client.get_avg_price(symbol=ticker)
    print("price → ", price['price'], "$", "\n")
    for interval in intervals:
        my_function(ticker, interval)

    print("\n", "╱", "Vwap 48: _______", "╲")
    if VwapPercent(ticker, Client.KLINE_INTERVAL_1DAY, 48) < 0:
        print("Day :", VwapPercent(
            ticker, Client.KLINE_INTERVAL_1DAY, 48), "   →", "Risky")
    else:
        print("Day :", VwapPercent(
            ticker, Client.KLINE_INTERVAL_1DAY, 48), "   →", "Safe")

    if VwapPercent(ticker, Client.KLINE_INTERVAL_4HOUR, 48) < 0:
        print("4h :", VwapPercent(ticker, "4h", 48), "   →", "Risky")
    else:
        print("4h :", VwapPercent(ticker, "4h", 48), "   →", "Safe")

    print('--------------------------')
