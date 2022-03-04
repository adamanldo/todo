from django.db import models
from django.utils import timezone

class Todo(models.Model):
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.details
