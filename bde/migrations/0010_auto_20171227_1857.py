# Generated by Django 2.0 on 2017-12-27 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0009_auto_20171227_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadgeneratedcontract',
            name='follow_up_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leadgeneratedcontract',
            name='follow_up_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 18, 57, 3, 478427)),
        ),
    ]
