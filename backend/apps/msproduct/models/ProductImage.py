from django.db import models
from utils import Model
from .Product import Product
from .Image import Image

class ProductImage(Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product'
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        db_column='image'
    )

    class Meta:
        db_table = 'MAE_PRODUCT_IMAGE'