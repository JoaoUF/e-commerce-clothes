from django.db import models
from utils import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
)
from .Price import Price


class Product(Model, TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, db_column="price")

    # def __str__(self) -> str:
    #     return self.title

    class Meta:
        db_table = "MAE_PRODUCT"
