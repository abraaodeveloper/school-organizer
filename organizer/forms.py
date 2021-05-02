from django import forms
from .models import *

class SemesterForm(forms.ModelForm):

    class Meta:
        model = Semester
        fields = ["id", "title", "description"]

class DisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = ["id", "title", "description"]

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "delivery_at"]