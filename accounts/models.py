from django.db import models


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
    category = models.CharField(max_length=100, verbose_name="Account Category")
    type = models.CharField(max_length=100, verbose_name="Account Type")
    balance = models.IntegerField(verbose_name="Account Balance")

    class Meta:
        verbose_name = "Account Projection"
        verbose_name_plural = "Account Projections"


class TransactionProjectionModel(models.Model):
    uuid = models.UUIDField(verbose_name="UUID", unique=True)
    account_id = models.CharField(max_length=100, verbose_name="Account ID")
    date = models.DateField(verbose_name="Date")
    payee_id = models.CharField(max_length=100, verbose_name="Payee ID")
    category_id = models.CharField(max_length=100, verbose_name="Category ID")
    memo = models.TextField(max_length=100, verbose_name="Memo")
    outflow = models.IntegerField(verbose_name="Outflow")
    inflow = models.IntegerField(verbose_name="Inflow")
    cleared = models.BooleanField(verbose_name="Cleared")

    class Meta:
        verbose_name = "Transaction Projection"
        verbose_name_plural = "Transaction Projections"