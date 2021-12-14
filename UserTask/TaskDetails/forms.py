from django.forms import ModelForm

from .models import *

class registerForm(ModelForm):
    class Meta:
        model=Users
        fields='__all__'   #for all fields

class addTaskForm(ModelForm):
    class Meta:
        model=Task
        fields='__all__'   #for all fields