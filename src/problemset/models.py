from django.db import models

from contests.models import Contest


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    categories = models.ManyToManyField(Category, related_name="problems")
    languages = models.ManyToManyField(Language, related_name="problems")
    time_limit = models.PositiveIntegerField()
    memory_limit = models.PositiveIntegerField()
    test_cases = models.FileField(upload_to="test_cases/")
    contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.PROTECT, related_name="problems")

    def __str__(self):
        return self.title
