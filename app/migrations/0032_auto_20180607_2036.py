# Generated by Django 2.0.5 on 2018-06-07 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20180607_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 7, 18, 36, 20, 50312, tzinfo=utc)),
        ),
    ]
