# Generated by Django 4.2.8 on 2023-12-30 21:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0007_alter_userproblem_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProblem",
        ),
    ]
