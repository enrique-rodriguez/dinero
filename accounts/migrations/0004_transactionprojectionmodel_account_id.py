# Generated by Django 5.0.6 on 2024-05-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_transactionprojectionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionprojectionmodel',
            name='account_id',
            field=models.CharField(default='', max_length=100, verbose_name='Account ID'),
            preserve_default=False,
        ),
    ]
