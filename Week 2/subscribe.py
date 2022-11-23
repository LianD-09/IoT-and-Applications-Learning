from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = 'iot_linhda'

# Client information
client_id = 'client_2'
username = 'linh_iot'
password = '12345'

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

def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

# Run
if __name__ == '__main__':
    client = connectMqtt()
    subscribe(client, topic)
    client.loop_forever()