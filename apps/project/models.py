import uuid
from datetime import datetime
from django.db import models
from accounts.models import CustomUser


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
