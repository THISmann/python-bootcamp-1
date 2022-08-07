from django.db import models
from datetime import datetime, date
#from studymanagement.models import *
#from studymanagement.models import *
# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone_numero = models.IntegerField()
    #etablissement = models.ForeignKey(Etablissement)
    # parent = models.OneToOneField(
    #     Parents,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )

    def __str__(self):
        return "%s the student" % self.username
    #parent = models.ForeignKey(Parents, on_delete=models.PROTECT)


class Teacher(models.Model):
    username = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    #topic = models.ForeignKey(Topic, on_delete=models.PROTECT)

    def __str__(self):
        return "%s the teacher is " % self.username


class Parents(models.Model):
    username = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255)
    students = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return "%s the username" % self.username
