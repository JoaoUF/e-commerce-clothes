from .base import *
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(ENV_DIR, '.env.development')
)

WSGI_APPLICATION = 'core.wsgi.development.application'

DEBUG = bool(int(os.environ.get('DEBUG', '1'))) # type: ignore
PRODUCTION = int(os.environ.get('PRODUCTION', '0')) # type: ignore
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ') # type: ignore
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(' ') # type: ignore

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