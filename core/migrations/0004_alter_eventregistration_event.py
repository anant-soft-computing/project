# Generated by Django 5.0 on 2023-12-28 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_registration_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.event'),
        ),
    ]
