# Generated by Django 2.0.5 on 2018-06-07 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180607_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 7, 14, 28, 30, 129460, tzinfo=utc)),
        ),
    ]
