set -o errexit
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist (password from DJANGO_SUPERUSER_PASSWORD env var)
python manage.py create_superuser --username syed --email syedmethappa0987@gmail.com || true