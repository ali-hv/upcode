# Generated by Django 4.2.8 on 2023-12-25 20:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
    ]
