import requests

class StockDataClient:
    BASE = {'stockdata': 'https://api.stockdata.org/v1/data/',
            'polygon': 'https://api.polygon.io/'}
    ENDPOINTS = {'stockdata': 
                    {'eod': 'eod',
                     'intra': 'intraday'},
                'polygon': 
                    {'ticker': 'v3/reference/tickers',
                     'div': 'v3/reference/dividends',
                     'market_holiday': 'v1/marketstatus/upcoming',
                     'market_now': 'v1/marketstatus/now',
                     'financials': 'vX/reference/financials'}}
    def __init__(self, api_keys: dict):
        self.api_keys = api_keys

    def __buildurl(self, ds, ep):
        return self.BASE[ds] + self.ENDPOINTS[ds][ep]
    
    def getgeneraldata(self, endpoint, ticker=None):
        DATASOURCE = 'polygon'
        url = self.__buildurl(DATASOURCE, endpoint)
        header = {'Authorization': 'Bearer ' + self.api_keys[DATASOURCE]}
        match endpoint:
            case 'ticker':
                r = requests.get(url=url+'/' + ticker, headers=header)
                return r.json()
            case 'div' | 'financials':
                r = requests.get(url=url + '?ticker='+ticker+'&limit=10', headers=header)
                return r.json()
            case 'market_holiday' | 'market_now':
                r = requests.get(url=url, headers=header)
                return r.json()
    
    def daily_data(self, endpoint, ticker, interval, date_from, date_to):
        DATASOURCE = 'stockdata'
        url = self.__buildurl(DATASOURCE, endpoint)
        header = {'Authorization': 'Bearer ' + self.api_keys[DATASOURCE]}
        r = requests.get(
            url=url 
            + '?symbols=' + ticker 
            + '&interval='+ interval 
            + '&date_from=' + date_from 
            + '&date_to=' + date_to, 
            headers=header
        )
        return r.json()

    