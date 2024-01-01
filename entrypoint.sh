# !/bin/sh
# Add the following line before starting your Django application
python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput
gunicorn project.wsgi:application --bind 0.0.0.0:8000

