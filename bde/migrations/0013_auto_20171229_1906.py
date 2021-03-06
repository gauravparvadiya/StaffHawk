# Generated by Django 2.0 on 2017-12-30 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0012_auto_20171227_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_type',
            field=models.CharField(default='1', max_length=3),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='contract_payment_type',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salescontract',
            name='contract_total_amount',
            field=models.CharField(default=1000, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadgeneratedcontract',
            name='follow_up_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 19, 6, 3, 180919)),
        ),
    ]
