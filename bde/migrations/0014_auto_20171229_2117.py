# Generated by Django 2.0 on 2017-12-30 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0013_auto_20171229_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_price',
            field=models.CharField(default=1000, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadgeneratedcontract',
            name='follow_up_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 21, 17, 21, 191176)),
        ),
    ]
