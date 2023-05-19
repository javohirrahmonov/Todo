from .models import *
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields ='__all__'