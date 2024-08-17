from __future__ import absolute_import
from django.conf import settings

if settings.PRODUCTION:
    from .celery import production_celery_app
    from .celery import stage_celery_app

    __all__ = ["production_celery_app", "stage_celery_app"]
else:
    from .celery import development_celery_app

    __all__ = ["development_celery_app"]
