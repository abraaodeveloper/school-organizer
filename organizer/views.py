from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from .models import Task, Semester, Discipline
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Home
def index(request):
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'guest/index.html', context)

# Semesters
@login_required
def semesterList(request):
    form = SemesterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = SemesterForm(request.POST)
            form.instance.user = request.user
            form.save()

    user = request.user
    semesters = user.semester_set.all()
    return render(request, 'logged/list_semesters.html', {'semesters': semesters, 'form':form})

# Discipline
@login_required
def disciplineList(request, semester_id):
    form = DisciplineForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = DisciplineForm(request.POST)
            form.instance.discipline = Semester.objects.get(semester=semester_id)
            form.save()

    if semester_id == 0:
        disciplines = Discipline.objects.all()
    else:
        disciplines = Discipline.objects.filter(semester=semester_id)
    return render(request, 'logged/list_disciplines.html', {'disciplines': disciplines, 'form':form, 'id': semester_id})

# Tasks
@login_required
def taskList(request, discipline_id):
    tasks = Task.objects.all()
    return render(request, 'logged/list_tasks.html', {'tasks': tasks})
