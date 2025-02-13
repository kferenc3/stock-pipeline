import boto3

class AwsClient:
    def __init__(self, profile, region='eu-central-1') -> None:
        self.session = boto3.Session(profile_name=profile, region_name=region)
    

    def dyamodb_get(self,key_name, key_value, table):
        dyndb = self.session.client('dyanamodb')
        response = dyndb.get_item(
            Key={
                key_name: {
                    'S': key_value
                },
            },
            TableName=table
        )
        return response
    def dynamodb_put():
        pass
    def dynamodb_update():
        pass

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