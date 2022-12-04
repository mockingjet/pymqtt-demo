import random, string, asyncio

from fastapi import FastAPI
from pymqtt_demo.demo3.mqtt_manager import MQTTManager

app = FastAPI()

# create manager
manager = MQTTManager("jetsai", "qwe123")

# create handler
handler = manager.create_client("handler")

# handle message from topic 'demo3' and return
def handler_callback(client, message):
    if message.topic == 'demo3':
        result =  'receive: ' + message.payload.decode("utf-8")
        client.publish('demo3-result', result)

handler.sub("demo3", handler_callback)

# create requester
requester = manager.create_client("requester")

requester.sub("demo3-result")

@app.get("/")
async def index():
    # publish a random text
    rdm = ''.join(random.choice(string.ascii_letters) for x in range(10))
    # send request message
    requester.pub('demo3', rdm)

    # wait for new message from topic 'demo3-result'
    while True:
        await asyncio.sleep(1)
        if len(requester.messages) > 0:
            text = requester.messages.pop().payload.decode("utf-8")
            return text