from django import forms
from .models import *

class SemesterForm(forms.ModelForm):

    class Meta:
        model = Semester
        labels  = {
            "id": "",
            "title": "Título", 
            "description": "Descrição"
        }
        fields = ["id", "title", "description"]

class DisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        labels  = {
            "id": "",
            "title": "Título", 
            "description": "Descrição"
        }
        fields = ["id", "title", "description"]

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        labels  = {
            "id": "",
            "title": "Título", 
            "description": "Descrição",
            "max_note": "Nota máxima", 
            "min_note": "Nota Mínima", 
            "state": "Andamento", 
            "delivery_at": "Data de entrega"
        }
        fields = ["id", "title", "description", "max_note", "min_note", "state", "delivery_at"]