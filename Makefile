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

check: lint test

lint:
	uv run ruff check task_manager

lint-fix:
	uv run ruff check task_manager --fix

i18n-ru:
	uv run manage.py makemessages -l ru

i18n-compile:
	uv run manage.py compilemessages

test:
	uv run manage.py test

test-users:
	uv run manage.py test task_manager.users

test-statuses:
	uv run manage.py test task_manager.statuses

test-tasks:
	uv run manage.py test task_manager.tasks

test-labels:
	uv run manage.py test task_manager.labels