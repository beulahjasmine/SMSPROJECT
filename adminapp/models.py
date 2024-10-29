from django.db import models
# Create your models here.


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class StudentList(models.Model):
    Register_Number= models.CharField(max_length=20, unique=True)
    Name=models.CharField(max_length=100)


def __str__(self):
    return self.Register_Number

