.PHONY: run makemigrations migrate createsuperuser shell test

run:
	python manage.py runserver

mk:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test
