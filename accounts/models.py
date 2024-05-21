from django.db import models

# Create your models here.



class AccountEventModel(models.Model):
    event_id = models.UUIDField(verbose_name="Event ID", unique=True)
    account_id = models.UUIDField(verbose_name="Account ID", unique=True)
    created_at = models.DateTimeField(verbose_name="Creation Datetime")
    event_name = models.CharField(max_length=100, verbose_name="Event Name")
    data = models.JSONField(verbose_name="Event Data")

    class Meta:
        verbose_name = "Account Event"
        verbose_name_plural = "Account Events"


class AccountProjectionModel(models.Model):
    uuid = models.UUIDField(verbose_name="UUID", unique=True)
    name = models.CharField(max_length=100, verbose_name="Account Name")
    type = models.CharField(max_length=100, verbose_name="Account Type")
    balance = models.IntegerField(verbose_name="Account Balance")

    class Meta:
        verbose_name = "Account Projection"
        verbose_name_plural = "Account Projections"