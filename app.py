import csv
from uuid import uuid4

import boto3
from chalice import Chalice

from chalicelib.db import Csv

s3 = boto3.client('s3', region_name='us-east-1')

app = Chalice(app_name='serverless-csv')
app.debug = True

@app.on_s3_event(bucket='samuelm333-csv', events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s", event.bucket, event.key)

    file = s3.get_object(Bucket=event.bucket, Key=event.key)

    lines = file['Body'].read().decode("utf-8").splitlines(True)
    reader = list(csv.reader(lines))

    headers = list(map(lambda header: header.lower().replace(" ", "_"), reader.pop(0)))

    for row in reader:
        data = dict(zip(headers, row))
        item = Csv(_id=str(uuid4()), **data)
        item.save()
