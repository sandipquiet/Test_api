# Generated by Django 3.2.6 on 2022-08-31 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20220831_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='completed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 12, 58, 32, 126286)),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 31, 12, 58, 32, 126286)),
        ),
    ]
