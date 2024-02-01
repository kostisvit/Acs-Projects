from django.forms import ModelForm
from .models import Todolist

class TodoListForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ('name', 'description','is_completed')