# Generated by Django 3.1.4 on 2021-01-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210125_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='first', max_length=255),
            preserve_default=False,
        ),
    ]
