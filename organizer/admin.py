from django.contrib import admin
from .models import Semester, Task, Discipline

# Register your models here.
admin.site.register(Semester)
admin.site.register(Task)
admin.site.register(Discipline)