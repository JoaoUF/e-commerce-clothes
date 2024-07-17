from django.db import models
from django.core.validators import MinValueValidator
from utils import Model
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from .Bill import Bill
from .Price import Price


class Item(Model, TimeStampedModel, ActivatorModel):
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        db_column="bill",
    )
    price = models.ForeignKey(Price, on_delete=models.CASCADE, db_column="price")
    quantity = models.IntegerField(
        db_column="quantity", validators=[MinValueValidator(1)]
    )

    class Meta:
        db_table = "MAE_ITEM"
