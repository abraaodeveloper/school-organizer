from django.db import models
from django.contrib.auth.models import User

class Semester(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Discipline(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
   
class Task(models.Model):

    STATUS = (
        ('doning', 'doning'), # fazendo
        ('done', 'done') # feito
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=6,  choices=STATUS) 
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
