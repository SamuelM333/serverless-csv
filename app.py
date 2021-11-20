import boto3
from chalice import Chalice

s3 = boto3.client('s3', region_name='us-east-1')
app = Chalice(app_name='serverless-csv')


@app.on_s3_event(bucket='csv', events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s", event.bucket, event.key)
    file = s3.get_object(Bucket=event.bucket, Key=event.key)
    data = file['Body'].read()
