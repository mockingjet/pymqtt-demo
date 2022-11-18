up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.dev.yml down

build:
	docker-compose -f docker-compose.dev.yml build

logs:
	docker-compose -f docker-compose.dev.yml logs

app-install:
	docker exec -it pymqtt-demo-app poetry install

app-sub:
	docker exec -it pymqtt-demo-app poetry run python pymqtt_demo/sub.py

app-pub:
	docker exec -it pymqtt-demo-app poetry run python pymqtt_demo/pub.py