# Generated by Django 2.0.5 on 2018-06-07 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180607_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 7, 13, 49, 11, 596742, tzinfo=utc)),
        ),
    ]
