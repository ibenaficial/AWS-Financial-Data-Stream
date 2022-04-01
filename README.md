# Streaming Financial Data with AWS Lambda

In this project, we use AWS Lambda to process and consume financial data of ten different stocks: Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX), Pinterest (PINS), Square (SQ), The Trade Desk (TTD), Okta (OKTA), Snap (SNAP), Datadog (DDOG). This is done using the [yfinance](https://pypi.org/project/yfinance/) API. 

To gather the data, we create a Lambda function and add a lambda layer where we write the code that collects data from yfinance and puts it into a firehouse data stream in AWS Kinesis. Then, using a Glue crawler, we're able to process the data and put it in to a schema. Using Athena, we're able to write and run queries. For this project, I wrote a query that gives us the highest hourly stock "high" price per company. 
