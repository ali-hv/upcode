# Generated by Django 4.2.8 on 2024-02-11 15:14

from django.db import migrations, models
import django.utils.timezone
import problemset.models


class Migration(migrations.Migration):
    dependencies = [
        ("problemset", "0015_remove_problem_test_cases_testcase"),
    ]

    operations = [
        migrations.AddField(
            model_name="problem",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="testcase",
            name="input_file",
            field=models.FileField(upload_to=problemset.models.input_path),
        ),
        migrations.AlterField(
            model_name="testcase",
            name="output_file",
            field=models.FileField(upload_to=problemset.models.output_path),
        ),
    ]