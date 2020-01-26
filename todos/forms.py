from django import forms #importneme forms
from .models import Todo # importneme si z modelov class Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title",)
        widgets = {'title':forms.TextInput(attrs = {"placeholder":"Tu napíš úlohu..."})}
