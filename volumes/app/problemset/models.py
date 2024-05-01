from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

import os

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
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="problems")
    languages = models.ManyToManyField(Language, related_name="problems")
    time_limit = models.PositiveIntegerField()
    memory_limit = models.PositiveIntegerField()
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    contest = models.ForeignKey(
        Contest,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="problems",
    )

    def __str__(self):
        return self.title

    def get_number_of_tries(self):
        submissions = self.submissions.all()
        solves = set([i.user_id for i in submissions if i.status != "waiting"])
        return len(solves)

    def get_number_of_solves(self):
        submissions = self.submissions.all()
        solves = set([i.user_id for i in submissions if i.status == "solved"])
        # unique_users = set(submission.user_id for submission in solves)
        return len(solves)

    def get_contest_page_url(self):
        if self.contest:
            return reverse('contests:contest_page', args=[self.contest.pk])


def input_path(instance, filename):
    # Produce the upload path of input files dynamically based on the problem pk
    problem_pk = str(instance.problem.pk)
    return os.path.join("testcases", problem_pk, "inputs", filename)


def output_path(instance, filename):
    # Produce the upload path of output files dynamically based on the problem pk
    problem_pk = str(instance.problem.pk)
    return os.path.join("testcases", problem_pk, "outputs", filename)


class TestCase(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="test_cases",
    )
    input_file = models.FileField(upload_to=input_path)
    output_file = models.FileField(upload_to=output_path)


class Submission(models.Model):
    STATUS_CHOICES = (
        ("solved", "Solved"),
        ("partial", "Partial"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="submissions")
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    submitted_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="submissions/")
    result = models.FileField(upload_to="submissions_results/", blank=True, null=True)
    score = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)], blank=True, null=True
    )

    def __str__(self):
        return self.problem.title

    @property
    def status(self):
        if self.score is None:
            return "waiting"
        elif self.score == 100:
            return "solved"
        return "partial"

    def get_judge_result(self):
        try:
            with open(self.result.path) as file:
                result = file.readlines()
        except ValueError:
            return None

        result = [i.strip() for i in result]
        return result

    def get_html_judge_result(self):
        html = ""

        if not self.get_judge_result():
            return ""

        for index, result in enumerate(self.get_judge_result()):
            html += f'<label style="color: #1645ff">Test { index+1 }</label><br>'
            if result == "Accepted":
                html += f'<label style="color: #219d25">{ result }</label><br>'
            elif result == "Wrong Answer":
                html += f'<label style="color: #9d2121">{ result }</label><br>'
            else:
                html += f'<label style="color: #daca0b">{ result }</label><br>'

        return html

    def get_code(self):
        try:
            with open(self.file.path) as file:
                file = file.readlines()
        except ValueError:
            return None

        file = [f"{str(index+1)} | {code}" for index, code in enumerate(file)]
        str_file = ""
        for i in file:
            str_file += i

        lexer = get_lexer_by_name(self.language.name, stripall=True)
        formatter = HtmlFormatter(full=True, style="emacs")
        return highlight(str_file, lexer, formatter)
