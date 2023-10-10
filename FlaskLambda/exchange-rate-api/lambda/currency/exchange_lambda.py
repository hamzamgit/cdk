import json
import os
import boto3
from datetime import timedelta, datetime

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']


def get_weekdays(start_date=None):
    if not start_date:
        start_date = datetime.today()
    week_no = start_date.weekday()
    if week_no == 0:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    elif week_no == 6:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    elif week_no == 5:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    else:
        current_date = start_date.strftime('%Y-%m-%d')
        last_day = start_date - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")

    return current_date, last_date


def get_currency_rates(today_currency, lastday_currency):
    """
    Extracts Comparison of the currency rate between current and previous currency differences.

    { "currency_code": {"today": rate, "difference": today rate - previous_rate}},
    { "currency_code": {"today": rate, "difference": today rate - previous_rate}},
    """
    return {
            x: {
                "today": float(today_currency["data"][x]),
                "difference": round(float(today_currency["data"][x]) - float(lastday_currency["data"][x]), 3)
            }
            for x, y in today_currency["data"].items()
    }


def lambda_handler(event, context):

    exchange_update_time = datetime.now()
    exchange_update_time.replace(hour=17)
    if datetime.now() > exchange_update_time:
        current_date, last_date = get_weekdays()
    else:
        current_date, last_date = get_weekdays(start_date=datetime.now() - timedelta(days=1))

    table = dynamodb.Table(TABLE_NAME)
    # Scan items in table for current, previous date
    try:
        today_currency = table.query(
            KeyConditionExpression=Key('id').eq(current_date)
        )
        last_date_currency = table.query(
            KeyConditionExpression=Key('id').eq(last_date)
        )

        response = get_currency_rates(today_currency["Items"][0], last_date_currency["Items"][0])
    except ClientError as e:
        response = e.response['Error']['Message']
        print(e.response['Error']['Message'])

    return {
        'response': response, 
        'statusCode': 200,
    }

print(lambda_handler(1,2))