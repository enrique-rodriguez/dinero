#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', connection_attempts=10, retry_delay=5))
channel = connection.channel()

channel.queue_declare(queue='hello')



for i in range(100):
    time.sleep(1)
    body = f'Hello World! {i}'
    channel.basic_publish(exchange='', routing_key='hello', body=body)
    print(f" [x] Sent {body}")



connection.close()