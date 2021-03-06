# Generated by Django 3.2.3 on 2021-08-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_artist_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='category',
            field=models.CharField(choices=[('BG', '남자 아이돌'), ('GG', '여자 아이돌'), ('HH', '랩/힙합'), ('ID', '인디음악'), ('BL', '발라드'), ('RB', '락밴드')], default='Boy Group', max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='group',
            field=models.CharField(choices=[('Solo', '솔로'), ('Duo', '듀오'), ('Quatro', '4인 그룹'), ('etc', '기타')], default='Solo', max_length=100),
        ),
    ]
