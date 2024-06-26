# Generated by Django 4.2.8 on 2023-12-26 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("detail", models.TextField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("registration_start_time", models.DateTimeField()),
                ("registration_end_time", models.DateTimeField()),
                ("is_active", models.BooleanField(default=False)),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="contests_participated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
