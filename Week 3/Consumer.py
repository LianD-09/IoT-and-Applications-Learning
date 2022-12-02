import pika
import sys
import os
import json


def main():
    credentials = pika.PlainCredentials(
        username='doanhlinh', password='20194314', erase_on_connect=True)
    parameters = pika.ConnectionParameters(
        host='localhost', port=5672, virtual_host='rabbitmq_linhda', credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test')

    # Since RabbitMQ works asynchronously, every time you receive a message, a callback function is called. We will simply print the message body to the terminal
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body))

    channel.basic_consume(
        queue='test', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
