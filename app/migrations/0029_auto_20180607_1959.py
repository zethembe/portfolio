# Generated by Django 2.0.5 on 2018-06-07 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20180607_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 7, 17, 59, 40, 146044, tzinfo=utc)),
        ),
    ]
