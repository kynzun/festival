# Generated by Django 3.2.3 on 2021-08-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210812_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='image_back_url',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='image_url',
        ),
        migrations.AddField(
            model_name='artist',
            name='enname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
