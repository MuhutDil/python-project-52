build:
	./build.sh

install:
	uv sync

collectstatic:
	uv run manage.py collectstatic

migrate:
	uv run manage.py migrate

dev:
	uv run manage.py runserver

start:
	uv run gunicorn task_manager.wsgi

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check task_manager

lint-fix:
	uv run ruff check task_manager --fix

