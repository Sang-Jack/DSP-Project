# Generated by Django 4.0.3 on 2022-04-30 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]