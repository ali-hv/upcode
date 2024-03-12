from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings

from contests.tasks import open_contest
from .models import Contest


@receiver(post_save, sender=Contest)
def open_contest_task(sender, instance, created, **kwargs):
    if not created:
        return
    
    start_time = instance.start_time
    now = timezone.now()

    delay = int((start_time - now).total_seconds())
    open_contest.apply_async(args=[instance.id], countdown=delay)