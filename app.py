import csv
from uuid import uuid4

import boto3
from chalice import Chalice

from chalicelib.db import Csv

s3 = boto3.client('s3', region_name='us-east-1')

app = Chalice(app_name='serverless-csv')
app.debug = True

# https://www.appsloveworld.com/sample-csv-file/
@app.on_s3_event(bucket='samuelm333-csv', events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s", event.bucket, event.key)

    file = s3.get_object(Bucket=event.bucket, Key=event.key)

    try
        lines = file['Body'].read().decode("utf-8").splitlines(True)
    except UnicodeDecodeError:
        app.log.error("Error decoding file")
        return

    reader = list(csv.reader(lines))

    try:
        headers = list(map(lambda header: header.lower().replace(" ", "_"), reader.pop(0)))
    except IndexError:
        app.log.error("IndexError")
        return

    for row in reader:
        data = dict(zip(headers, row))
        try:
            item = Csv(_id=str(uuid4()), **data)
            item.save()
        except ValueError:
            app.log.error("ValueError")
