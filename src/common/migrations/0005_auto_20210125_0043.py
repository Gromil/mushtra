# Generated by Django 3.1.4 on 2021-01-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20210125_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_fio',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telegram_username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
