from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Task


@receiver(post_delete, sender=Task)
def update_removed_tasks_count(sender, instance, **kwargs):
    if instance.performer:
        performer = instance.performer
        performer.removed_tasks_count += 1
        performer.save()
