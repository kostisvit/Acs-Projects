import uuid,os
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

def custom_upload_path(instance, filename):
    # Get the related model's name and use it in the file path
    project = instance.project.name if instance.project else 'no_related_name'
    sanitized_model_name = project.replace(' ', '_').replace('-', '_').replace('|', '_')  # Add more replacements as needed
    
    # Use os.path.join for constructing the file path
    return os.path.join('custom_directory', sanitized_model_name, filename)
    #return f'custom_directory/{project}/{filename}'

class ProjectFile(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    attachment = models.FileField(upload_to=custom_upload_path)

    def __str__(self):
        return self.name



class ProjectNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name