# import the models package. This line is already existing as soon as we use 'startapp'
from django.db import models

# Must inherit from Django Model class


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    #number_pet = models.IntegerField(max_value=10)
