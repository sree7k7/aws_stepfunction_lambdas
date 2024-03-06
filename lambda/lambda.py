import os
import json
import boto3

def lambda_handler(event, context):
    # if aws account 
    print("event: ", event)
    print(len(event['accountNo']))
    x = len(event['accountNo'])
    if x == 12:
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid account number')
        }