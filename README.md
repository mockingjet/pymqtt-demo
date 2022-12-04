# Pymqtt Demo

## Getting Started

```bash
$ make up

# demo1
$ make demo1

# demo2
$ make demo2
# see http://localhost:8000/push and http://localhost:8000/pull

# demo3
$ make demo3
# see http://localhost:8000
```

| demos |                                               |
| ----- | --------------------------------------------- |
| demo1 | 讓多個 MQTT Clients 可以同時收到消息          |
| demo2 | 在 http server 可以 push / pull 消息          |
| demo2 | 對 http server 發請求後可回傳 mqtt 的 message |
