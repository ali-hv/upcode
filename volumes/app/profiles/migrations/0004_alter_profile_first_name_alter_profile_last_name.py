# Generated by Django 4.2.8 on 2023-12-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0003_alter_profile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
