from .base import *
from dotenv import load_dotenv, dotenv_values

load_dotenv(dotenv_path=os.path.join(ENV_DIR, ".env.development"))

WSGI_APPLICATION = "core.wsgi.development.application"
DEBUG = bool(int(os.environ.get("DEBUG", "1")))  # type: ignore
PRODUCTION = int(os.environ.get("PRODUCTION", "0"))  # type: ignore
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(" ")  # type: ignore
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "").split(" ")  # type: ignore
INTERNAL_IPS = os.environ.get("INTERNAL_IPS", "").split(" ")  # type: ignore
HOST_URL_SITE = os.environ.get("HOST_URL_SITE", "http://localhost:3030")

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

# RABBITMQ
RABBIT_USER = os.environ.get("RABBIT_USER")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_HOST = os.environ.get("RABBIT_HOST")

# CELERY
BROKER_URL = f"amqp://{RABBIT_USER}:{RABBIT_PASSWORD}@localhost:5672/{RABBIT_HOST}"
CELERY_RESULT_BACKEND = "amqp://localhost:5672"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

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

# STATIC FILE
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfields")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafields")

# DJANGO REST AUTH
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("SOCIALACCOUNT_GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("SOCIALACCOUNT_GOOGLE_CLIENT_ID"),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
}

# STRIPE
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
stripe.api_key = STRIPE_SECRET_KEY
