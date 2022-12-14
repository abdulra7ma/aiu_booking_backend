# Generated by Django 4.1.3 on 2022-11-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="useraccount",
            options={},
        ),
        migrations.RemoveField(
            model_name="useraccount",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="useraccount",
            name="last_name",
        ),
        migrations.AddField(
            model_name="useraccount",
            name="student_id",
            field=models.CharField(
                default=1,
                max_length=128,
                unique=True,
                verbose_name="Student ID",
            ),
            preserve_default=False,
        ),
    ]
