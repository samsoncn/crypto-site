import ccxt
from ccxt.binance import binance
import pprint

binance_exchange = ccxt.binance()
binance_markets = binance_exchange.load_markets()
# print(binance_markets)

ticker_data = binance_exchange.fetch_tickers()

with open("output.txt", "w") as txt_file:
    # txt_file.write(str(pprint.pformat(binance_markets)))

    # market information - each coin
    # txt_file.write(str(pprint.pformat(binance_markets['LIT/USDT'])))
    txt_file.write(str(pprint.pformat(ticker_data)))


