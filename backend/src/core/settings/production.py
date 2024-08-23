from .base import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(ENV_DIR, ".env.production"))

WSGI_APPLICATION = "core.wsgi.production.application"
DEBUG = True
PRODUCTION = True
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")  # type: ignore
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")  # type: ignore
CORS_ALLOW_CREDENTIALS = True
INTERNAL_IPS = os.environ.get("INTERNAL_IPS").split(" ")  # type: ignore
HOST_URL_SITE = os.environ.get("HOST_URL_SITE")

# DATABASES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": int(os.environ.get("POSTGRES_PORT", "5432")),  # type: ignore
    }
}

# EMAIL
EMAIL_USE_TLS = bool(int(os.environ.get("EMAIL_USE_TLS")))  # type: ignore
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))  # type: ignore
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# CACHE
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# RABBITMQ
RABBIT_USER = os.environ.get("RABBITMQ_USERNAME")
RABBIT_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
RABBIT_HOST = os.environ.get("RABBITMQ_HOST")

# CELERY
BROKER_URL = f"amqp://{RABBIT_USER}:{RABBIT_PASSWORD}@localhost:5672/{RABBIT_HOST}"
CELERY_RESULT_BACKEND = "amqp://localhost:5672"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# STATIC FILE
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfields")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafields")
