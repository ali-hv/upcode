from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"


class Language(models.Model):
    name = models.CharField(max_length=30)


class Problem(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    categories = models.ManyToManyField(Category, related_name="problems")
    languages = models.ManyToManyField(Language, related_name="problems")
    time_limit = models.PositiveIntegerField()
    memory_limit = models.PositiveIntegerField()
    test_cases = models.FileField(upload_to="test_cases/")
    # contest = models.ForeignKey(Contest, blank=True)
