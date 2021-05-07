from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('achievement/', views.achievement, name='achievement'),

    path('semesters-list/', views.semesterList, name='semesterlist'),
    path('disciplines-list/<int:semester_id>/', views.disciplineList, name='disciplinelist'),
    path('tasks-list/<int:discipline_id>', views.taskList, name='tasklist'),
    path('deletediscipline/<int:discipline_id>/<int:semester_id>/', views.deletediscipline, name='deletediscipline'),
    path('tasks-list/taskalter/<int:discipline_id>/<int:task_id>/<state>', views.taskAlter, name='taskalter'),
    path('tasks-list/deletetask/<int:discipline_id>/<int:task_id>/', views.deletetask, name='deletetask'),
]
