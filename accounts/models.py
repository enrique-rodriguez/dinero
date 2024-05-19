import uuid
from django.db import models

# Create your models here.


class AccountModel(models.Model):
    uuid = models.UUIDField(verbose_name="UUID", unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"