from django.db import models
from django.core.validators import MinValueValidator
from utils import Model
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from .Product import Product
from .Bill import Bill


class Item(Model, TimeStampedModel, ActivatorModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product")
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        db_column="bill",
        null=True,
    )
    quantity = models.IntegerField(
        db_column="quantity", validators=[MinValueValidator(1)]
    )

    def get_price(self):
        return self.product.price.discountPrice

    class Meta:
        db_table = "MAE_ITEM"
