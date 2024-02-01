from django.forms import ModelForm

from .models import ProjectFile, Project


class ProjectFileForm(ModelForm):
    class Meta:
        model = ProjectFile
        fields = ('name', 'attachment',)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description','is_completed')