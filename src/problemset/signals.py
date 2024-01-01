from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Submission

from threading import Thread

from .scripts import judge_submission


@receiver(post_save, sender=Submission)
def judge_submission_handler(sender, instance, created, **kwargs):
    if not created:
        return

    judge_thread = Thread(target=judge_submission, args=[instance])
    judge_thread.start()
