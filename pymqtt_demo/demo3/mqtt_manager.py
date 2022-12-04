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
        client = MQTTClient(name)
        client.connect(self.username, self.password, self.host, self.port, self.keepalive)
        self.clients.update({name: client})
        return client


class MQTTClient:
    def __init__(self, name:str):
        self._client = mqtt.Client(userdata=name)
        self._client.on_connect = self.on_connect
        self._client.on_message = self.on_message
        self.messages =[]
        self.callbacks = {}

    def connect(self, username:str, password:str, host:str, port:int, keepalive:int):
        self._client.username_pw_set(username, password)
        self._client.connect(host, port, keepalive)
        self._client.loop_start()

    def sub(self, topic:str, callback=None):
        self._client.subscribe(topic)   
        if callback:
            self.callbacks.update({topic: callback})

    def pub(self, topic:str, payload:any):
        self._client.publish(topic, payload)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f'{userdata}: connected!')
        else:
            print(f'{userdata}: connect failed!')

    def on_message(self, client, userdata, message):
        self.messages.append(message)
        
        callback  = self.callbacks.get(message.topic)
        if callback:
            callback(client, message)