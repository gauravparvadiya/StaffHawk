# Generated by Django 2.0 on 2017-12-27 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0005_auto_20171227_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='project_attachment',
            field=models.FileField(max_length=200, upload_to=''),
        ),
    ]