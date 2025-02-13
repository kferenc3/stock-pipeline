import os
import boto3
import requests
import json
from datetime import datetime, timedelta, UTC
import time
from libs.stockdata import StockDataClient

APIKEYS={'stockdata': os.environ.get('STOCKDATA'),
         'polygon': os.environ.get('POLYGON')}

client = StockDataClient(APIKEYS)
today = datetime.date(datetime.now(UTC))
fivedaysago = today + timedelta(days=-5)
#AWS ARN: 'arn:aws:iam::891377129971:user/stock-python'
#print(client.daily_data('intra', 'PM','hour',datetime.strftime(fivedaysago,'%Y-%m-%d'),datetime.strftime(today,'%Y-%m-%d')))
#print(client.getgeneraldata('market_now'))
events = {'market':'', 'general':'', 'div':'', 'minute':'', 'eod':'', 'hist_div':''}
def create_event(event):
    session = boto3.Session(profile_name='<>',region_name='eu-central-1')
    dyndb = session.client('dynamodb')
    for ev_type in event.keys():
        response = dyndb.get_item(
            Key={
                'event_type': {
                    'S': ev_type
                },
            },
            TableName='event_run_details'
        )
        event[ev_type] = response['Item']['last_run_dt']['S']
    return event

print(create_event(events))
""" response = dyndb.put_item(
    Item = {
        'event_type': {
            'S': 'hist_div',
        },
        'last_run_dt': {
            'S': '1900-01-01'
        }
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='event_run_details'
) """

""" response = dyndb.update_item(
    ExpressionAttributeNames={
        '#D': 'last_run_dt',
    },
    ExpressionAttributeValues={
        ':d': {
            'S': '1910-12-31',
        },
    },
    Key={
        'event_type': {
            'S': 'general',
        },
    },
    ReturnValues='ALL_NEW',
    TableName='event_run_details',
    UpdateExpression='SET #D = :d',
) """


#s3 = session.client('s3')

"""  'general': {
            'S': '1900-01-01',
        },
        'div': {
            'S': '1900-01-01',
        },
        'minute': {
            'S': '1900-01-01',
        },
        'eod': {
            'S': '1900-01-01',
        },
        'hist_div': {
            'S': '1900-01-01',
        } """

#response = s3.list_buckets()
#for bucket in response['Buckets']:
#    print(f'Bucket Name: {bucket["Name"]}')

'''
Scenario 1: refresh market holidays - 1/week (market upcoming - polygon)
Scenario 2: get general financials 1/month/ticker (financials + ticker - polygon)
Scenario 3: Get dividends from the previous month 1/month/ticker (div - polygon)
Scenario 4: Get previous day's minute-level data 1/day/ticker (intra - stockdata)
Scenario 5: EoD historical load ad-hoc/ticker (eod - stockdata)
Scenario 6: Historical dividends ad-hoc/ticker (div - polygon)
'''

'''
Event types: market, general, div, minute, eod, hist_div
'''


#tickers = ['PM', 'LMT', 'IBM', 'NVDA', 'PDM', 'O', 'GOOG', 'NKE', 'AGNC', 'AMZN', 'AMCR', 'NESN', 'SNOW', 'EVO']
tickers = ['AGNC','AMZN','AMCR','GOOG','IBM','LMT','NKE','NVDA','PM','PDM','O','SNOW']
""" for ticker in tickers:
    r = requests.get('https://api.stockdata.org/v1/entity/search?search=' + ticker + '&api_token=<>')
    with open(ticker+'.json', 'w+') as f:
        json.dump(r.json(),f) """


#client = StockDataClient(APIKEYS)

""" for ticker in tickers:
    print('-----------------------------------------------')
    print(ticker)
    print(client.getgeneraldata('ticker',ticker))
    time.sleep(12) """


#print(client.daily_data('intra','PM','minute','2024-08-16','2024-08-19'))

#print(json_content['type'])