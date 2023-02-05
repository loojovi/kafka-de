import os
import json

from kafka import KafkaConsumer
from time import sleep
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    os.environ.get('KAFKA_TOPIC'),
    bootstrap_servers=[os.environ.get('BROKER_IP')],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

s3 = S3FileSystem()
for count, i in enumerate(consumer):
    with s3.open(f"s3://{os.environ.get('S3_BUCKET')}/file_{count}.json", 'w') as file:
        json.dump(i.value, file)
    