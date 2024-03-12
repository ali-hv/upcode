from django.shortcuts import get_object_or_404
from django.utils import timezone
from celery import shared_task
from config.celery import app

from .models import Contest


@shared_task
def open_contest(contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    contest.is_active = True
    contest.save()

    return "Contest activated successfully"
