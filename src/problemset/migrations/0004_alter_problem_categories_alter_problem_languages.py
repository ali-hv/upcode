# Generated by Django 4.2.8 on 2023-12-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("problemset", "0003_rename_category_problem_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="categories",
            field=models.ManyToManyField(
                related_name="problems", to="problemset.category"
            ),
        ),
        migrations.AlterField(
            model_name="problem",
            name="languages",
            field=models.ManyToManyField(
                related_name="problems", to="problemset.language"
            ),
        ),
    ]