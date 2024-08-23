from .base import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(ENV_DIR, ".env.development"))

# DJANGO

INSTALLED_APPS += [
    "drf_yasg",
    "debug_toolbar",
    "silk",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
]

WSGI_APPLICATION = "core.wsgi.development.application"
DEBUG = True
PRODUCTION = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")  # type: ignore
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")  # type: ignore
CORS_ALLOW_CREDENTIALS = True
INTERNAL_IPS = os.environ.get("INTERNAL_IPS").split(" ")  # type: ignore
HOST_URL_SITE = os.environ.get("HOST_URL_SITE")

# DEGUB TOOLBAR
# DEFAULT - https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "cachalot.panels.CachalotPanel",
]

# SILKY
# DEFAULT - https://silk.readthedocs.io/en/latest/configuration.html
SILKY_AUTHENTICATION = False  # User must login
SILKY_AUTHORISATION = False  # User must have permissions

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
RABBIT_USER = os.environ.get("RABBITMQ_DEFAULT_USER")
RABBIT_PASSWORD = os.environ.get("RABBITMQ_DEFAULT_PASS")
RABBIT_HOST = os.environ.get("RABBITMQ_DEFAULT_VHOST")

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
