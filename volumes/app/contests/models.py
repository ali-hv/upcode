from django.utils import timezone
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Contest(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    registration_start_time = models.DateTimeField()
    registration_end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    participants = models.ManyToManyField(
        User, related_name="contests_participated", blank=True
    )

    def __str__(self):
        return self.name

    def is_registration_open(self):
        now = timezone.now()
        return self.registration_start_time <= now <= self.registration_end_time

    def is_contest_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    def duration(self):
        return self.end_time.hour - self.start_time.hour
