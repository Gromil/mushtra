# Generated by Django 3.1.4 on 2021-01-24 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mushtra', '0002_auto_20210125_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='created_at', verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='modified_at', verbose_name='modified_at')),
                ('description', models.CharField(default='', max_length=255)),
                ('state', models.CharField(choices=[('done', 'done'), ('skipped', 'skipped'), ('failed', 'failed'), ('inactive', 'inactive')], max_length=125)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mushtra.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
