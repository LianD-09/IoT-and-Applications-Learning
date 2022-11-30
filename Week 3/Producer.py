import pika, json

data = {
    "id": 11,
    "packet_no": 126,
    "temperature": 30,
    "humidity": 60,
    "tds": 1100,
    "pH": 5.0
}

credentials = pika.PlainCredentials(
    username='doanhlinh', password='20194314', erase_on_connect=True)
parameters = pika.ConnectionParameters(
    host='localhost', port=5672, virtual_host='rabbitmq_linhda', credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test')
channel.basic_publish(exchange='', routing_key='test', body=json.dumps(data))
print(" [x] Sent %r" % data)

connection.close()
