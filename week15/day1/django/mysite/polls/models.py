# import the models package. This line is already existing as soon as we use 'startapp'
from django.db import models

# Must inherit from Django Model class


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    #number_pet = models.IntegerField(max_value=10)


class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_role = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    done_task = models.BooleanField()
    number_hour = models.IntegerField()
