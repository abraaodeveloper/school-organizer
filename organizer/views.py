from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm

from .models import Task

def index(request):
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'guest/index.html', context)

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'logado/tasks/list-tasks.html', {'tasks': tasks})

def task(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'logado/tasks/task.html', {'task': task})