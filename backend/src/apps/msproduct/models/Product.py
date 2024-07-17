from utils import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
)


class Product(Model, TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel):
    class Meta:
        db_table = "MAE_PRODUCT"
