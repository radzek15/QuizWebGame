#docker
build:
	docker-compose up  --build --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs

logs-api:
	docker-compose logs api

makemigrations:
	docker-compose run --rm api python manage.py makemigrations

migrate:
	docker-compose run --rm api python manage.py migrate

collectstatic:
	docker-compose run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker-compose run --rm api python manage.py createsuperuser

down-v:
	docker-compose down -v

inspect-pg:
	docker volume inspect imageapi_development_postgres_data

connect_pg:
	docker-compose exec postgres psql --username=radzek15 --dbname=quiz_db

clear-cont:
	docker container prune -f

clear-vol:
	docker volume prune -f

clear-net:
	docker network prune -f

clear-im:
	docker image prune -a -f

clear-all:
	docker system prune -a

#===============================================================================================================================================================
#pre-commit
pre-commit:
	pre-commit run --all-files --hook-stage=commit

diff:
	pre-commit run --all-files --no-apply --diff
