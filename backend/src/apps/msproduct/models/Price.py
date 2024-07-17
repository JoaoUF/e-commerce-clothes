from django.db import models
from utils import Model
from django_extensions.db.models import TimeStampedModel
from .Color import Color
from .Size import Size
from .Product import Product


class Price(TimeStampedModel, Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        db_column="color",
    )
    size = models.ForeignKey(Size, on_delete=models.CASCADE, db_column="size")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column="product"
    )
    originalPrice = models.DecimalField(
        max_digits=19, decimal_places=2, db_column="original_price"
    )
    discountPrice = models.DecimalField(
        max_digits=19, decimal_places=2, db_column="discount_price"
    )

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = "MAE_PRICE"
