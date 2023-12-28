from django.templatetags.static import static
from django.conf import settings
from django.db import models

from problemset.models import Problem

User = settings.AUTH_USER_MODEL


class UserProblem(models.Model):
    STATUS_CHOICES = (
        ("solved", "Solved"),
        ("partial", "Partial"),
        ("no-try", "No try"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="users")
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return self.problem.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static("base/icons/default-avatar.png")
