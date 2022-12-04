up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

build:
	docker-compose -f docker-compose.yml build

logs:
	docker-compose -f docker-compose.yml logs

bash:
	docker exec -it pymqtt-demo-app bash

demo1:
	docker exec -it pymqtt-demo-app python pymqtt_demo/demo1/main.py 

demo2:
	docker exec -it pymqtt-demo-app uvicorn pymqtt_demo.demo2.main:app --reload --host 0.0.0.0

demo3:
	docker exec -it pymqtt-demo-app uvicorn pymqtt_demo.demo3.main:app --reload --host 0.0.0.0