from .base import *
from dotenv import load_dotenv, dotenv_values

load_dotenv(
    dotenv_path=os.path.join(ENV_DIR, '.env.development')
)

WSGI_APPLICATION = 'core.wsgi.development.application'

DEBUG = bool(int(os.environ.get('DEBUG', '1'))) # type: ignore
PRODUCTION = int(os.environ.get('PRODUCTION', '0')) # type: ignore
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ') # type: ignore
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(' ') # type: ignore

HOST_URL_SITE = os.environ.get('HOST_URL_SITE', 'http://localhost:3030')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432')) # type: ignore
    }
}

EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS'))) # type: ignore
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT')) # type: ignore
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')