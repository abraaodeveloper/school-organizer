from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):

    STATUS = (
        (1, 'doning'), # fazendo
        (2, 'done') # feito
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=1,  choices=STATUS) 
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title