from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    path('taskslist', views.taskList, name='tasklist'),
    path('task', views.task, name='tasklist'),

]