# Generated by Django 2.0 on 2018-01-02 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0016_auto_20180102_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadgeneratedcontract',
            name='today_follow_up',
        ),
        migrations.AddField(
            model_name='contract',
            name='today_follow_up',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='leadgeneratedcontract',
            name='follow_up_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 1, 57, 34, 98627)),
        ),
    ]