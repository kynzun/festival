# Generated by Django 3.2.3 on 2021-08-12 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210812_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='image_back',
        ),
    ]