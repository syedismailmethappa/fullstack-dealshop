import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR


ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTNAME")]
CSRF_TRUSTED_ORIGINS = ['https://' + host for host in os.environ.get("RENDER_EXTERNAL_HOSTNAME")]

DEBUG = False
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", SECRET_KEY)

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOWED_ORIGINS = [
    "https://fullstack-dealshop2.onrender.com",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

STORAGES={
    "default":{
        "BACKEND":"django.core.files.storage.FileSystemStorage"
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

DATABASES = {
    'default': dj_database_url.config(  
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}
