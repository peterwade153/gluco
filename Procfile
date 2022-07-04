release: python manage.py migrate --no-input
web: gunicorn app.wsgi:application --log-file -
