from django import forms
from .models import Task 

class TaskForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TimeInput({'placeholder':'Add task here'}))
    class Meta:
        model =Task
        fields= ['content']
        
class updateTaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields= '__all__'