import json
import boto3
import random
import datetime
import yfinance as yf

kinesis = boto3.client('kinesis', "us-east-2")

def lambda_handler(event, context):
    stock = ["FB", "SHOP", "BYND", "NFLX", "PINS", "SQ", "TTD", "OKTA", "SNAP", "DDOG"]
    start_date = "2021-11-30"
    end_date = "2021-12-01"
    stock_interval = "5m"
    for stock in stock:
        ticker = yf.Ticker(stock)
        hist = ticker.history(
                    start = start_date, 
                    end = end_date, 
                    interval = stock_interval)
        for index, row in hist.iterrows():
            json_string = json.dumps({
                            "high": "{:.2f}".format(row["High"]), 
                            "low": "{:.2f}".format(row["Low"]), 
                            "ts": index.strftime('%Y-%m-%d %H:%M:%S'), 
                            "name": stock
            })+"\n"
            kinesis.put_record(
                StreamName = "sta9760f2021bena-stream2", 
                Data = json_string, 
                PartitionKey = "partitionkey")
    return {
        'statusCode':200, 
        'body': json_string
    }