from django.db import models
from utils import Model
from django_extensions.db.models import TimeStampedModel


class Size(TimeStampedModel, Model):
    name = models.CharField(
        db_column="name",
        max_length=50,
    )

    def __str__(self) -> str:
        return str(self.id) + self.name

    class Meta:
        db_table = "MAE_SIZE"
