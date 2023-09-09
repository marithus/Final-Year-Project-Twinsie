release: python manage.py makemigrations
release: python manage.py migrate
web: daphne Twinsie.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=Twinsie.settings -v2