from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from .models import Task, Semester, Discipline
from django.contrib.auth.decorators import login_required


# Home
def index(request):
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'guest/index.html', context)

# Semesters
@login_required
def semesterList(request):
    user = request.user
    print(user)
    semesters = user.semester_set.all()
    return render(request, 'logged/list_semesters.html', {'semesters': semesters})

# Discipline
@login_required
def disciplineList(request, semester_id):
    disciplines = Discipline.objects.filter(semester=semester_id)
    return render(request, 'logged/list_disciplines.html', {'disciplines': disciplines})

# Tasks
@login_required
def taskList(request, discipline_id):
    tasks = Task.objects.filter("discipline", discipline_id)
    return render(request, 'logged/list_tasks.html', {'tasks': tasks})
