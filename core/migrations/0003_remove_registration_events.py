# Generated by Django 5.0 on 2023-12-28 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_eventregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='events',
        ),
    ]
