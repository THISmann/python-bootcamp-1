# import the models package. This line is already existing as soon as we use 'startapp'
from django.db import models
from datetime import datetime, date

# Must inherit from Django Model class


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    #number_pet = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year-self.birth_date.year
        return f'{current_age}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=50)
    released_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    # If you delete a person, his posts will be also deleted

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_role = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    done_task = models.BooleanField()
    number_hour = models.IntegerField()
