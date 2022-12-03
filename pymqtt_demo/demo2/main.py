from fastapi import FastAPI
from pymqtt_demo.demo2.mqtt_manager import MQTTManager

app = FastAPI()

topic = "demo2"
texts = []

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'{userdata}: connected!')
        client.subscribe(topic)
    else:
        print(f'{userdata}: connect failed!')

def on_message(client, userdata, message):
    text = message.payload.decode("utf-8")
    texts.append(text)

manager = MQTTManager("jetsai", "qwe123")

pusher = manager.create_client("pusher")
pusher.on_connect = on_connect
# pusher.on_message = on_message
manager.connect(pusher)

puller = manager.create_client("puller")
puller.on_connect = on_connect
puller.on_message = on_message
manager.connect(puller)

@app.get("/push")
def push():
    pusher.publish(topic, 'pushing')
    return 'pushed'

@app.get('/pull')
def pull():
    return texts