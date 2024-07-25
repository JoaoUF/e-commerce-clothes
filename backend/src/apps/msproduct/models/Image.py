from django.db import models
from .Product import Product
from utils import Model
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Image(Model, TimeStampedModel, TitleSlugDescriptionModel):
    upload = models.ImageField(upload_to="products/%Y/%m/%d/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product")

    class Meta:
        db_table = "MAE_IMAGE"
