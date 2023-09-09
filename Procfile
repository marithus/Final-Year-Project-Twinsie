web: daphne Twinsie.asgi:application --port $PORT --bind 0.0.0.0 -v2
web: python manage.py runserver
chatworker: python manage.py runworker --settings=Twinsie.settings -v2