from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
import os

from .models import ProjectFile

@receiver(pre_delete, sender=ProjectFile)
def delete_files_and_folder(sender, instance, **kwargs):
    # Get the path of the file
    file_path = instance.attachment.path

    # If the file exists, delete it
    if os.path.exists(file_path):
        os.remove(file_path)

    # Get the directory containing the file
    folder_path = os.path.dirname(file_path)

    # If the directory exists and is empty, delete it
    if os.path.exists(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)
