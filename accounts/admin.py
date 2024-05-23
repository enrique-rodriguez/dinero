from django.contrib import admin

from accounts import models

# Register your models here.

admin.site.register(models.AccountEventModel)
admin.site.register(models.AccountProjectionModel)
admin.site.register(models.TransactionProjectionModel)
