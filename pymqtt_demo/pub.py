import paho.mqtt.client as mqtt


class MQTTPublisher:
    def __init__(self, user:str, passwd:str, topic:str):
        self.topic = topic
        self.client = mqtt.Client()
        self.client.username_pw_set(user, passwd)
        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("MQTT publisher connected!")
        else:
            print("MQTT publisher fails to connect with returned code =",rc)

    def connect(self, host="mosquitto", port=1883, keepalive=60):
        self.client.connect(host, port, keepalive)

    def publish(self, msg:str):
        self.client.publish(self.topic, msg)

if __name__ == '__main__':
    sub = MQTTPublisher("jetsai", "qwe123", "Pymqtt/Demo")
    sub.connect()
    sub.publish("test")
