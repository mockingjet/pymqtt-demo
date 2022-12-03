up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

build:
	docker-compose -f docker-compose.yml build

logs:
	docker-compose -f docker-compose.yml logs

demo1:
	docker exec -it pymqtt-demo-app poetry run python pymqtt_demo/demo1/main.py 