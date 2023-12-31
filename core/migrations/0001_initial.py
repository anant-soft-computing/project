# Generated by Django 5.0 on 2023-12-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('event_location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('batch_year', models.IntegerField(blank=True, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('tshirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large')], max_length=3, null=True)),
                ('registration', models.BooleanField(blank=True, default=False, null=True)),
                ('kit', models.BooleanField(default=False)),
                ('tshirt', models.BooleanField(default=False)),
                ('cap', models.BooleanField(default=False)),
                ('lapel_pin', models.BooleanField(default=False)),
                ('barcode', models.ImageField(blank=True, null=True, upload_to='images')),
                ('events', models.ManyToManyField(blank=True, to='core.event')),
            ],
        ),
    ]
