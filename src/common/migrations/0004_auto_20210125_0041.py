# Generated by Django 3.1.4 on 2021-01-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
