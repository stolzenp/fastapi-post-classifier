# variables
IMAGE_NAME = instagram-post-classifier-api
CONTAINER_NAME = instagram-post-classifier-api-container
PORT = 8000

.PHONY: up down restart logs clean test coverage lint lint-black lint-ruff format

# docker compose commands
up:
	docker compose up -d

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f

clean:
	docker compose down --rmi local

# test commands
test:
	pytest tests/

coverage:
	pytest --cov=app tests/

# linter commands
lint: lint-black lint-ruff

lint-black:
	black --check .

lint-ruff:
	ruff check .

# format commands
format:
	black .
	ruff check --fix .
