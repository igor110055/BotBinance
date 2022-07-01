import get_data as gd
import pandas as pd
import pandas_ta as ta
from binance.client import Client
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


Tickers = ['BTCUSDT', 'ETHUSDT', 'NEOUSDT', 'LTCUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'LINKUSDT', 'WAVESUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'PERLUSDT', 'DENTUSDT', 'KEYUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BUSDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RVNUSDT', 'NKNUSDT', 'STXUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'VITEUSDT', 'FTTUSDT', 'OGNUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'STPTUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'CHRUSDT', 'GXSUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'LRCUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'PAXGUSDT',
           'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'FIOUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'UTKUSDT', 'XVSUSDT', 'NEARUSDT', 'FILUSDT', 'CTKUSDT', 'AXSUSDT', 'DNTUSDT', 'XEMUSDT', 'SKLUSDT', 'GRTUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT', 'PONDUSDT', 'ALICEUSDT', 'SUPERUSDT', 'CFXUSDT', 'EPSUSDT', 'TKOUSDT', 'PUNDIXUSDT', 'TLMUSDT', 'FORTHUSDT', 'SLPUSDT', 'ICPUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT', 'XVGUSDT', 'GTCUSDT', 'TORNUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'DEXEUSDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'XECUSDT', 'ELFUSDT', 'POLYUSDT', 'VIDTUSDT', 'GALAUSDT', 'ILVUSDT', 'SYSUSDT', 'CVPUSDT', 'AGLDUSDT', 'RADUSDT', 'RAREUSDT', 'LAZIOUSDT', 'CHESSUSDT', 'ADXUSDT', 'DARUSDT', 'BNXUSDT', 'MOVRUSDT', 'ENSUSDT', 'KP3RUSDT', 'PORTOUSDT', 'POWRUSDT', 'VGXUSDT', 'JASMYUSDT', 'AMPUSDT', 'PLAUSDT', 'RNDRUSDT', 'SANTOSUSDT', 'FLUXUSDT', 'FXSUSDT', 'VOXELUSDT', 'HIGHUSDT', 'CVXUSDT', 'SPELLUSDT', 'ACHUSDT', 'GLMRUSDT', 'LOKAUSDT', 'API3USDT', 'ALPINEUSDT', 'TUSDT', 'ASTRUSDT', 'GMTUSDT', 'KDAUSDT', 'APEUSDT', ]


def VwapPercent(ticker, interval, peroid):
    data = gd.get_klines(ticker, interval, "1400 hours ago UTC+1")

    vwapp = vwap(data, peroid)
    LastOneVwap = vwapp.iloc[-1]
    klines = client.get_avg_price(symbol=ticker)
    klines = float(klines['price'])

    return (klines - LastOneVwap) / klines * 100


data = []

for ticker in Tickers:
    data.append((ticker, VwapPercent(ticker, Client.KLINE_INTERVAL_4HOUR, 84),))


df = pd.DataFrame(data, columns=['symbol', 'vwapPercent'])
df = df.sort_values('vwapPercent')

print(df)
