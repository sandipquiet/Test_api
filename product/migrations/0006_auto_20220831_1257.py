# Generated by Django 3.2.6 on 2022-08-31 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='completed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 12, 57, 3, 30101)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 12, 57, 3, 30101)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='mobile',
            field=models.IntegerField(max_length=12),
        ),
    ]
