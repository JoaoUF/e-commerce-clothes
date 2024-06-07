from django.db import models
from utils import Model # type: ignore
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

class Template(TimeStampedModel, TitleDescriptionModel, Model):
    html = models.TextField(
        db_column='html'
    )

    class Meta:
        db_table = 'MAE_TEMPLATE'