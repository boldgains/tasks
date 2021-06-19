from datetime import datetime

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    date_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=Todo)
# def create_date_completed(sender, instance, created, **kwargs):
#     print('post save running')
#     if instance.is_complete and instance.date_completed:
#         instance.date_completed = datetime.now()
#         instance.save()
#     print('datetime complete saved')
