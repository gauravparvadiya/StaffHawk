# Generated by Django 2.0 on 2017-12-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0004_auto_20171227_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='project_attachment',
            field=models.FileField(max_length=200, upload_to='media/attachments/'),
        ),
    ]
