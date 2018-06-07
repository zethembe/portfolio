# Generated by Django 2.0.5 on 2018-06-07 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20180607_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 7, 14, 57, 56, 890890, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
