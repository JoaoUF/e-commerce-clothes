from django.db import models
from msauthentication.models import CustomUser
from utils import Model
from django_extensions.db.models import TimeStampedModel

class Bill(Model, TimeStampedModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        db_column='user'
    )
    total = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        db_column='total'
    )

    class Meta:
        db_table= 'MAE_BILL',
