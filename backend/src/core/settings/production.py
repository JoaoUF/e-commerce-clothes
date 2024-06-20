from .base import *
from dotenv import dotenv_values

config = dotenv_values(".env.production")

WSGI_APPLICATION = 'core.wsgi.development.application'

DEBUG = bool(int(config.get('DEBUG', '1'))) # type: ignore
PRODUCTION = int(config.get('PRODUCTION', '0')) # type: ignore
SECRET_KEY = config.get('SECRET_KEY')
ALLOWED_HOSTS = config.get('DJANGO_ALLOWED_HOSTS', '').split(' ') # type: ignore
CORS_ALLOWED_ORIGINS = config.get('CORS_ALLOWED_ORIGINS', '').split(' ') # type: ignore

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get('POSTGRES_DB'),
        'USER': config.get('POSTGRES_USER'),
        'PASSWORD': config.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': int(config.get('POSTGRES_PORT', '5432')) # type: ignore
    }
}
