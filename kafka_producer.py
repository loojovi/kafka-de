import time
import json
import random
import os

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=[os.environ.get('BROKER_IP')], 
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    # Simulate streaming to test_topic
    producer.send(os.environ.get('KAFKA_TOPIC'), value={'random_num': f'{random.randint(0,100)}'})
    time.sleep(2)