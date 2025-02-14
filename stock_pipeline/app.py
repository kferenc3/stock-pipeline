import os
import yfinance as yf
from polygon import RESTClient
from libs.stockdata import StockDataClient
import polars as pl

APIKEYS={'stockdata': os.environ.get('STOCKDATA'),
         'polygon': os.environ.get('POLYGON')}

data = yf.Ticker('AAPL')
info = {k: v for k, v in data.info.items() if k not in ['companyOfficers']}
# print(data.history(period='1d', interval='1m'))
# print(pl.DataFrame(info))
# print(pl.DataFrame(data.info).select(pl.col('companyOfficers')).unnest('companyOfficers'))

# pl.DataFrame(data.info).drop(['companyOfficers', 'longBusinessSummary']).write_csv('info.csv')
# print(data.history(period='1d', interval='1m'))
df = pl.from_pandas(data.financials, include_index=True)
# print(data.financials.to_dict())

col_names = df.select(pl.nth(0)).transpose().to_dicts()
col_names[0]['column'] = 'Dates'
df.drop_in_place('None')
df = df.transpose(include_header=True)
df = df.rename(col_names[0])
# print(df)

# df = df.transpose(include_header=False) #.with_columns(pl.Series(name='Date', values=['2024-09-30', '2023-09-30', '2022-09-30', '2021-09-30', '2020-09-30']))
# with pl.Config(set_fmt_float='full', float_precision=None, thousands_separator=' ', tbl_hide_dataframe_shape=True, tbl_hide_dtype_separator=True, tbl_hide_column_data_types=True):
#     print(df[['EBIT', 'Tax Rate For Calcs', 'Total Revenue']]
#       .with_columns(pl.col('EBIT').mul(1-pl.col('Tax Rate For Calcs')).alias('NOPAT')))
    

print(data.recommendations)





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