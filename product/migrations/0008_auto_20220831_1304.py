# Generated by Django 3.2.6 on 2022-08-31 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220831_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='completed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 13, 4, 33, 92813)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 13, 4, 33, 92813)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
