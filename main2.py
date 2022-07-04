Aymen, [04-07-2022 15:23]
import get_data as gd
from tradingview_ta import TA_Handler
import pandas as pd
import pandas_ta as ta
import binance.client
from binance.client import Client
import os
import requests

Pkey = ""
Skey = ""
client = Client(api_key=Pkey, api_secret=Skey)


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

    return float((klines-LastOneVwap)/klines*100)


tickers = ['BTCUSDT', 'ETHUSDT', 'NEOUSDT', 'LTCUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'LINKUSDT', 'WAVESUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'PERLUSDT', 'DENTUSDT', 'KEYUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BUSDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RVNUSDT', 'NKNUSDT', 'STXUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'VITEUSDT', 'FTTUSDT', 'OGNUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'STPTUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'CHRUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'LRCUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'PAXGUSDT',
           'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'FIOUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'UTKUSDT', 'XVSUSDT', 'NEARUSDT', 'FILUSDT', 'CTKUSDT', 'AXSUSDT', 'DNTUSDT', 'XEMUSDT', 'SKLUSDT', 'GRTUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT', 'PONDUSDT', 'ALICEUSDT', 'SUPERUSDT', 'CFXUSDT', 'TKOUSDT', 'PUNDIXUSDT', 'TLMUSDT', 'FORTHUSDT', 'SLPUSDT', 'ICPUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT', 'XVGUSDT', 'GTCUSDT', 'TORNUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'DEXEUSDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'XECUSDT', 'ELFUSDT', 'POLYUSDT', 'VIDTUSDT', 'GALAUSDT', 'ILVUSDT', 'SYSUSDT', 'CVPUSDT', 'AGLDUSDT', 'RADUSDT', 'RAREUSDT', 'LAZIOUSDT', 'CHESSUSDT', 'ADXUSDT', 'DARUSDT', 'BNXUSDT', 'MOVRUSDT', 'ENSUSDT', 'KP3RUSDT', 'PORTOUSDT', 'POWRUSDT', 'VGXUSDT', 'JASMYUSDT', 'AMPUSDT', 'PLAUSDT', 'RNDRUSDT', 'SANTOSUSDT', 'FLUXUSDT', 'FXSUSDT', 'VOXELUSDT', 'HIGHUSDT', 'CVXUSDT', 'SPELLUSDT', 'ACHUSDT', 'GLMRUSDT', 'LOKAUSDT', 'API3USDT', 'ALPINEUSDT', 'TUSDT', 'ASTRUSDT', 'GMTUSDT', 'KDAUSDT', 'APEUSDT', ]

Aymen, [04-07-2022 15:23]
intervals = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d", "1M"]
switcher = {
    0: 60,
    1: 60,
    2: 60,
    3: 60,
    4: 3600,
    5: 3600,
    6: 3600,
    7: 86400,
    8: 2592000
}

depths = ["1 minute", "5 minutes", "15 minutes", "30 minutes",
          "1 hour", "2 hours", "4 hours", "1 day", "1 month"]


def GetTPS(ticker, interval):
    global switcher
    global intervals
    Data = client.get_historical_klines(
        ticker, interval,  str(depths[intervals.index(interval)]) + ' ago UTC+1')
    t = interval[:-1]
    mins = int(switcher[intervals.index(interval)]*int(t))
    Data = pd.DataFrame(Data)
    Data.columns = ['TimeStamp', 'Open_Price', 'High_Price', 'Low_Price', 'Close_Price',
                    'Volume', 'Ignore', 'Quote_Volume', 'Num_Trade', 'Buy_Volume', 'Buy_Vol_Val', 'x']
    TPSNow = float(Data['Num_Trade'].mean())/mins
    TPSNow = round(TPSNow, 3)
    return TPSNow


def GetVolume(ticker, interval):
    global switcher
    global intervals
    Data = client.get_historical_klines(
        ticker, interval,  str(depths[intervals.index(interval)]) + ' ago UTC+1')

    Data = pd.DataFrame(Data)
    Data.columns = ['TimeStamp', 'Open_Price', 'High_Price', 'Low_Price', 'Close_Price',
                    'Volume', 'Ignore', 'Quote_Volume', 'Num_Trade', 'Buy_Volume', 'Buy_Vol_Val', 'x']
    Volume = float(Data['Quote_Volume'])
    Volume = round(Volume, 1)
    return Volume


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
            TPSnow = GetTPS(ticker, interval)
            volume = GetVolume(ticker, interval)
            msg = str("╔" + str(interval) + ":" + "\n" + "TPS : " + str(TPSnow) + " " + "\n" + "Volume : " + str(volume) + " $" + "\n" + "Summary :" +
                      str(global_detail['RECOMMENDATION']) + "\nMOVING AVERAGES :" + str(global_detail1['RECOMMENDATION']) + "\n" + "oscillators :" + str(global_detal2['RECOMMENDATION']) + "╝" + "\n" )
    except Exception as e:
        msg = str(e)
        msg += "\n"
    return msg


loop = True
while loop:
    for ticker in tickers:
        price = client.get_avg_price(symbol=ticker)

        message = str("→" + ticker + "←" + "\n"+"price → " +
                      price['price'] + "$" + "\n"+"\n")
        for interval in intervals:
            message += str(my_function(ticker, interval))

        message += str("\n" + "╱" + "Vwap 48: _______" + "╲"+"\n"+"\n")
        if VwapPercent(ticker, Client.KLINE_INTERVAL_1DAY, 48) < 0:
            message += str("Day :" + str(VwapPercent(ticker,
                                                     Client.KLINE_INTERVAL_1DAY, 48)) + "   →" + "Risky  🔴" + "\n"+"\n")
        else:
            message += str("Day :" + VwapPercent(ticker,
                                                 Client.KLINE_INTERVAL_1DAY, 48) + "   →" + "Safe   🟢" + "\n"+"\n")

        if VwapPercent(ticker, Client.KLINE_INTERVAL_4HOUR, 48) < 0:
            message += str("4h :" + str(VwapPercent(ticker, "4h", 48)) +
                           "   →" + "Risky  🔴" + "\n"+"\n")
        else:
            message += str("4h :" + str(VwapPercent(ticker, "4h", 48)) +
                           "   →" + "Safe   🟢" + "\n"+"\n")

        message += str('--------------------------' + "\n"+"\n")

        sendMsg(message)
