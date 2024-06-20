from django.db import models
from src.utils import Model
from django_extensions.db.models import TimeStampedModel

class Color(TimeStampedModel, Model):
    name = models.CharField(
        db_column='name',
        max_length=50,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table= 'MAE_COLOR'
