# Generated by Django 3.2.6 on 2021-08-23 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='duration',
        ),
    ]
