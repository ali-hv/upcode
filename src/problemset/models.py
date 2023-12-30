from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db import models

from contests.models import Contest

User = settings.AUTH_USER_MODEL


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Problem(models.Model):
    LEVEL_CHOICES = (
        ("easy", "ساده"),
        ("intermediate", "متوسط"),
        ("hard", "سخت"),
    )

    title = models.CharField(max_length=255)
    detail = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="problems")
    languages = models.ManyToManyField(Language, related_name="problems")
    time_limit = models.PositiveIntegerField()
    memory_limit = models.PositiveIntegerField()
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    test_cases = models.FileField(upload_to="test_cases/")
    contest = models.ForeignKey(
        Contest,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="problems",
    )

    def __str__(self):
        return self.title

    def get_number_of_solves(self):
        users = self.users.all()
        solves = [i for i in users if i.status == "solved"]
        return len(solves)


class Submission(models.Model):
    STATUS_CHOICES = (
        ("solved", "Solved"),
        ("partial", "Partial"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="users")
    file = models.FileField(upload_to="submissions/")
    result = models.FileField(upload_to="submissions_results/", blank=True, null=True)
    score = models.PositiveIntegerField(validators=[MaxValueValidator], blank=True, null=True)

    def __str__(self):
        return self.problem.title

    @property
    def status(self):
        if not self.score:
            return "waiting"
        elif self.score == 100:
            return "solved"
        return "partial"
