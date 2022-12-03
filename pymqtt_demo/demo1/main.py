import time
import paho.mqtt.client as mqtt


class MQTTManager:
    def __init__(self, username:str, password:str, host="mosquitto", port=1883, keepalive=60):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.keepalive= keepalive
        self.topics = []
        self.clients = {}
     
    def create_client(self, name: str):
        client = mqtt.Client(userdata=name)
        self.clients.update({name: client})
        client.username_pw_set(self.username, self.password)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.host, self.port, self.keepalive)
        client.loop_start()
        return client
        
    def add_topic(self, topic:str):
        self.topics.append(topic)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f'{userdata}: connected!')
            for topic in self.topics:
                client.subscribe(topic)
        else:
            print(f'{userdata}: connect failed!')

    def on_message(self, client, userdata, message):
        print(f'{userdata}: received [{message.topic}]:{message.payload.decode("utf-8")}')

if __name__ == '__main__':
    manager =  MQTTManager("jetsai", "qwe123")
    manager.add_topic('demo')
    
    for i in range(3):
        manager.create_client('sub'+str(i))

    pub = manager.create_client('pub')
    while True:
        time.sleep(5)
        pub.publish('demo', 'test')
