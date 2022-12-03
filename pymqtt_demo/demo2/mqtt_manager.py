import paho.mqtt.client as mqtt


class MQTTManager:
    def __init__(self, username:str, password:str, host="mosquitto", port=1883, keepalive=60):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.keepalive= keepalive
        self.clients = {}
     
    def create_client(self, name: str):
        client = mqtt.Client(userdata=name)
        self.clients.update({name: client})
        client.username_pw_set(self.username, self.password)
        return client
    
    def connect(self, client):
        client.connect(self.host, self.port, self.keepalive)
        client.loop_start()

