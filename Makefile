up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.dev.yml down

build:
	docker-compose -f docker-compose.dev.yml build

logs:
	docker-compose -f docker-compose.dev.yml logs