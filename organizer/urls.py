from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('semesters-list/', views.semesterList, name='semesterlist'),
    path('disciplines-list/<int:discipline_id>/', views.disciplineList, name='tasklist'),
    path('tasks-list/', views.taskList, name='tasklist'),
]
