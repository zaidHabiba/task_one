# Generated by Django 2.2.3 on 2020-01-07 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200106_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmapper',
            name='shorten_url',
        ),
    ]