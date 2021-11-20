from chalice import Chalice

app = Chalice(app_name='serverless-csv')


@app.on_s3_event(bucket='csv', events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s", event.bucket, event.key)
