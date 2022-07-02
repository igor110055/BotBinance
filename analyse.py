import requests
import json
import pandas as pd
import numpy as np
import datetime as dt
import time
import binance.client
from binance.client import Client
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def sendMsg(message):
    token = '5538213713:AAGuVpkfvhXneQ9vdBxtE5DTMGKoC7A773E'
    groupId = 'JusstATessting'
    msg = f'Hello from Python'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
    res = requests.get(url)
    if res.status_code == 200:
        print('Successfully sent')
    else:
        print('ERROR: Could not send Message')


tickers = ['BTCUSDT', 'GNOUSDT', 'COCOSUSDT', 'LOKAUSDT', 'ETHUSDT', 'SOLUSDT', 'ADAUSDT', 'XRPUSDT', 'USDCUSDT',
           'DOTUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LUNAUSDT', 'LTCUSDT', 'BUSDUSDT', 'ALGOUSDT', 'LINKUSDT', 'BCHUSDT', 'AXSUSDT',
           'XLMUSDT', 'MANAUSDT', 'VETUSDT', 'ICPUSDT', 'EGLDUSDT', 'FILUSDT', 'TRXUSDT', 'FTTUSDT', 'THETAUSDT', 'ETCUSDT', 'HBARUSDT',
           'ATOMUSDT', 'SANDUSDT', 'FTMUSDT', 'NEARUSDT', 'XTZUSDT', 'GRTUSDT', 'XMRUSDT', 'GALAUSDT', 'HNTUSDT', 'EOSUSDT', 'FLOWUSDT', 'KLAYUSDT',
           'LRCUSDT', 'STXUSDT', 'KSMUSDT', 'BTTUSDT', 'MKRUSDT', 'ZECUSDT', 'ENJUSDT', 'XECUSDT', 'ONEUSDT', 'NEOUSDT', 'CHZUSDT', 'AMPUSDT',
           'WAVESUSDT', 'QNTUSDT', 'BATUSDT', 'CRVUSDT', 'HOTUSDT', 'ARUSDT', 'DASHUSDT', 'CELOUSDT', 'TFUELUSDT', 'XEMUSDT', 'QTUMUSDT', 'IOTXUSDT',
           'DCRUSDT', 'MINAUSDT', 'VGXUSDT', 'TUSDUSDT', 'ZENUSDT', 'ANKRUSDT', 'LPTUSDT', 'ICXUSDT', 'OMGUSDT', 'WAXPUSDT', 'SCUSDT', 'RVNUSDT',
           'ROSEUSDT', 'ZILUSDT', 'USDPUSDT', 'BNTUSDT', 'ZRXUSDT', 'HIVEUSDT', 'STORJUSDT', 'ONTUSDT', 'SNXUSDT', 'SKLUSDT', 'KAVAUSDT', 'IOSTUSDT',
           'OCEANUSDT', 'MOVRUSDT', 'ALICEUSDT', 'POLYUSDT', 'REQUSDT', 'CELRUSDT', '1INCHUSDT', 'NUUSDT', 'FETUSDT', 'SYSUSDT', 'CHRUSDT', 'LSKUSDT',
           'MDXUSDT', 'CTSIUSDT', 'DENTUSDT', 'SXPUSDT', 'COTIUSDT', 'WRXUSDT', 'OGNUSDT', 'BTCSTUSDT', 'CVCUSDT', 'VTHOUSDT', 'NKNUSDT', 'ARDRUSDT',
           'BAKEUSDT', 'CFXUSDT', 'OXTUSDT', 'RLCUSDT', 'POLSUSDT', 'POWRUSDT', 'ONGUSDT', 'STMXUSDT']


Pkey = '9vFJDkbgWm09axRIfJoIXqfdLTBpUtD9jNGXmE5x04VhANKd1x0eCLcD11OmfyRS'
Skey = 'XS0pbBZSYLx0C8Zie0o02QwA3fFj6bBV2I3ncgy95a7DNK0Jc2vPgZDpekv08hP5'
client = Client(api_key=Pkey, api_secret=Skey)
df = pd.DataFrame(columns=['symbol', 'TPS', 'TPS_Change'])


def getdata(ticker, df=df):
    Data = client.get_historical_klines(
        ticker, '30m', '4 hours ago UTC+1')
    Data = pd.DataFrame(Data)
    Data.columns = ['TimeStamp', 'Open_Price', 'High_Price', 'Low_Price', 'Close_Price',
                    'Volume', 'Ignore', 'Quote_Volume', 'Num_Trade', 'Buy_Volume', 'Buy_Vol_Val', 'x']
    TPSNow = float(Data['Num_Trade'].mean())/1800
    idx = tickers.index(ticker)
    if os.path.exists('TPS.csv'):
        df1 = pd.read_csv('TPS.csv')
        TPSBefore = float(df1.loc[df1['symbol'] == ticker]['TPS'].values[0])
        TPSChangeNow = (TPSNow-TPSBefore)/TPSBefore*100
        df.loc[idx] = [ticker, TPSNow,
                       round(TPSChangeNow, 3)]
    else:
        df.loc[idx] = [ticker, TPSNow, 0.0]


def main():
    with ThreadPoolExecutor(max_workers=1000) as executor:
        executor.map(getdata, tickers)


loop = True

while loop:
    main()
    df.TPS = df.TPS.astype(float)
    df.TPS_Change = df.TPS_Change.astype(float)
    df = df.sort_values(by=['TPS', 'TPS_Change'], ascending=False)
    df.to_csv('TPS.csv', index=False)
    msg = df.head(10)
    sendMsg(msg)
    time.sleep(90)
