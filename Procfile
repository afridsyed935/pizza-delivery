release: python manage.py migrate --no-input
web gunicorn postgressdb.wsgi --log-file -