# Generated by Django 3.2.3 on 2021-08-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
