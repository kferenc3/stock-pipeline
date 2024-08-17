import os
from libs.stockdata import StockDataClient

APIKEYS={'stockdata': os.environ.get('STOCKDATA'),
         'polygon': os.environ.get('POLYGON')}

client = StockDataClient(APIKEYS)

print(client.getgeneraltickerdata('ticker', 'PM'))
print(client.getgeneraltickerdata('financials', 'PM'))
print(client.getgeneraltickerdata('div', 'PM'))