# Generated by Django 4.1.3 on 2022-11-27 05:04

import datetime
import uuid

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="updated"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(db_index=True, default=True),
                ),
                (
                    "name",
                    models.CharField(max_length=256, verbose_name="Facility"),
                ),
                ("bio", models.TextField(verbose_name="Facility Bio")),
                (
                    "image",
                    models.FileField(blank=True, upload_to="facilities"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="updated"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(db_index=True, default=True),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.date(2022, 11, 27),
                        verbose_name="Booking date",
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(verbose_name="Start time date"),
                ),
                ("end_time", models.TimeField(verbose_name="End time date")),
                (
                    "facility",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="booking.facility",
                        verbose_name="Booked Facility",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
