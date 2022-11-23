import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = 'iot_linhda'

# Client information
client_id = 'client_1'
username = 'linh_iot'
password = '12345'

data = {
    "id": 11,
    "packet_no": 126,
    "temperature": 30,
    "humidity": 60,
    "tds": 1100,
    "pH": 5.0
}


def createClient(client_id, username, password):
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    return client

def connectMqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = createClient(client_id, username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, data):
    while True:
        result = client.publish(topic, data)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{data}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(3)

# Run
if __name__ == '__main__':
    client = connectMqtt()
    client.loop_start()
    publish(client, str(data))
