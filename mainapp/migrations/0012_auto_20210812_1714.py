# Generated by Django 3.2.3 on 2021-08-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210812_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='enname',
        ),
        migrations.AddField(
            model_name='artist',
            name='image_back_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='image_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
