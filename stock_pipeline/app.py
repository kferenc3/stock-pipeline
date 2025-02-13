import os
import yfinance as yf
from libs.stockdata import StockDataClient
import polars as pl

APIKEYS={'stockdata': os.environ.get('STOCKDATA'),
         'polygon': os.environ.get('POLYGON')}


data = yf.Ticker('AAPL')


for k in data.info.keys():
    pass

print(data.quarterly_income_stmt)
# print(data.history(period='1d', interval='1m'))
# df = pl.from_pandas(data.financials, include_index=True)
# print(df.select(pl.nth(0)).transpose().to_dict(as_series=False))

# col_names = df.select(pl.nth(0)).transpose().to_dicts()
# col_names[0]['column'] = 'Dates'
# df.drop_in_place('None')
# df = df.transpose(include_header=True)
# df = df.rename(col_names[0])
# print(df)

# df = df.transpose(include_header=False) #.with_columns(pl.Series(name='Date', values=['2024-09-30', '2023-09-30', '2022-09-30', '2021-09-30', '2020-09-30']))

# print(df[['EBIT', 'Tax Rate For Calcs', 'Total Revenue']])
# print(df.filter(items=['EBIT', 'Tax Rate For Calcs', 'Total Revenue'], axis='index'))




# NOPAT, NOPAT yield, ROC és Sales Growth
# NOPAT = EBIT * (1 - Tax Rate)
# For this calculation, you need:
# EBIT (Earnings Before Interest and Taxes)
# Tax Rate

# 2. NOPAT Yield Calculation:
# NOPAT Yield = NOPAT / Total Revenue
# For this calculation, you need:
# NOPAT (Net Operating Profit After Taxes)
# Total Revenue