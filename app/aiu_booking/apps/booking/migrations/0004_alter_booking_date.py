# Generated by Django 4.1.3 on 2022-12-13 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_rename_uuid_booking_id_rename_uuid_facility_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 13, 9, 33, 20, 634206, tzinfo=datetime.timezone.utc), verbose_name='Booking date'),
        ),
    ]
