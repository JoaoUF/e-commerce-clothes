from django.db import models
from django.core.validators import MinValueValidator
from src.utils import Model
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from .Product import Product
from .Bill import Bill

class Item(Model, TimeStampedModel, ActivatorModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product'
    )
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        db_column='bill',
        null=True,
    )
    quantity = models.IntegerField(
        db_column='quantity',
        validators=[MinValueValidator(1)]
    )
    total = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        db_column='total'
    )

    class Meta:
        db_table= 'MAE_ITEM'
