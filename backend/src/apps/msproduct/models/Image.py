from django.db import models
from src.utils import Model
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

class Image(Model, TimeStampedModel, TitleSlugDescriptionModel):
    upload = models.ImageField(
        upload_to='products/%Y/%m/%d/'
    )

    class Meta:
        db_table= 'MAE_IMAGE'
