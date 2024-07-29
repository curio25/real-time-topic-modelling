import boto3
import json
import pandas as pd
import time

# Initialize the Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-2')

# Function to simulate real-time data ingestion
def send_data_to_kinesis(data, stream_name):
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey="partition_key"
    )
    return response