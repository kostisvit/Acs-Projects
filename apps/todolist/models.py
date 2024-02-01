import uuid
from datetime import datetime, timezone
from django.db import models

from accounts.models import CustomUser
from project.models import Project


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Todolist(TimeStampMixin):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, related_name='todolists', on_delete=models.CASCADE)

    
    def mark_as_completed(self):
        self.is_completed = True
        self.completion_date = timezone.now().date()
        self.save()
        
    def __str__(self):
        return self.name
