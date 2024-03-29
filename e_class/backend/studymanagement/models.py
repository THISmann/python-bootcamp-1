from django.db import models
from datetime import datetime, date
from authentifications.models import Teacher
from backend import *

# Create your models here.


class Classe(models.Model):
    name = models.CharField(max_length=255)
    #head_teacher = models.ForeignKey(to, on_delete)
    # define the head teacher who will manage the class

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone_numero = models.IntegerField()
    content = models.CharField(max_length=255)
    Teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    create_at = models.DateField(max_length=55)
    number_of_hour = models.IntegerField()
    #etablissement = models.ForeignKey(Etablissement)

    def __str__(self):
        return self.name


class Homework(models.Model):
    #topic = models.ManyToManyField(to=topic )
    #course = models.ManyToManyField()
    #classe = models.ManyToManyField()
    content = models.CharField(max_length=255)
    create_at = models.DateField()
    date_end = models.DateField()
    #author = models.ForeignKey(to=Teacher)

    def __str__(self):
        return self.topic

    pass


class Topic(models.Model):
    name = models.CharField(max_length=255)
    #classes = models.ForeignKey(Classe, on_delete=models.PROTECT)
    #instructor = models.ManyToManyField()

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
