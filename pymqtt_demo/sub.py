import time
import paho.mqtt.client as mqtt


class MQTTSubscriber:
    def __init__(self, user:str, passwd:str, topic:str, meta:str):
        self.topic = topic
        self.client = mqtt.Client(userdata=meta)
        self.client.username_pw_set(user, passwd)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f'[Sub-{userdata}] MQTT subcriber connected!')
            client.subscribe(self.topic)
        else:
            print("MQTT subcriber fails to connect with returned code =",rc)

    def on_message(self, client, userdata, message):
        print(f'[Sub-{userdata}] received message "{message.payload.decode("utf-8")}" on topic *{message.topic}* with Qos {str(message.qos)}')

    def connect(self, host="mosquitto", port=1883, keepalive=60):
        self.client.connect(host, port, keepalive)
        self.client.loop_start()


if __name__ == '__main__':
    for i in range(10):
        sub = MQTTSubscriber("jetsai", "qwe123", "Pymqtt/Demo", str(i))
        sub.connect()

    while True:
        time.sleep(1)