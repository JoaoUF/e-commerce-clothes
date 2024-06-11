from __future__ import absolute_import

from .celery import development_celery_app
from .celery import production_celery_app
from .celery import stage_celery_app