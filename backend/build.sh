set -o errexit
pip install -r backend/requirements.txt

pytthon manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput