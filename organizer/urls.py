from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('semesters-list/', views.semesterList, name='semesterlist'),

    path('disciplines-list/<int:semester_id>/', views.disciplineList, name='disciplinelist'),
    path('tasks-list/<int:discipline_id>', views.taskList, name='tasklist'),

    path('tasks-list/taskalter/<int:discipline_id>/<int:task_id>/<state>', views.taskAlter, name='taskalter'),
]
