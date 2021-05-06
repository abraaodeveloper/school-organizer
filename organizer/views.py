from django.shortcuts import render, get_object_or_404, redirect
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
    context = {'form': form, "optionsmenu": 1}
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
    return render(request, 'logged/list_semesters.html', {'semesters': semesters, 'form':form, "optionsmenu": 1})

# Discipline
@login_required
def disciplineList(request, semester_id):
    form = DisciplineForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.semester = Semester.objects.get(id=semester_id)
            form.save()

    if semester_id == 0:
        disciplines = Discipline.objects.all()
    else:
        disciplines = Discipline.objects.filter(semester=semester_id)
    return render(request, 'logged/list_disciplines.html', {'disciplines': disciplines, 'form':form, 'id': semester_id, "optionsmenu": 2})

# Tasks
@login_required
def taskList(request, discipline_id):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.discipline = Discipline.objects.get(id=discipline_id)
            form.save()
    tasks = None
    if discipline_id == 0:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(discipline=discipline_id)
    return render(request, 'logged/list_tasks.html', {'tasks': tasks, 'form':form, "iddiscipline": discipline_id, "optionsmenu": 3})

# Tasks modifier
@login_required
def taskAlter(request, discipline_id, task_id, state):

    task = Task.objects.get(id = task_id)
    task.state = state
    task.save()

    return redirect('/tasks-list/'+str(task.discipline.id))