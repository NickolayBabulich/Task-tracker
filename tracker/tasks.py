from celery import shared_task
from django.utils import timezone


@shared_task
def delete_expired_tasks():
    from tracker.models import Task
    expired_tasks = Task.objects.filter(deadline__lt=timezone.now())
    for task in expired_tasks:
        task.delete()
