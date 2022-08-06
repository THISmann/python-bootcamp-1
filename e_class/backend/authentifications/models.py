from django.db import models
from datetime import datetime, date
from studymanagement.models import *
# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone_numero = models.IntegerField()
    #etablissement = models.ForeignKey(Etablissement)
    #parent = models.ForeignKey(Parents, on_delete=models.PROTECT)


class Teacher(models.Model):
    username = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    #topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    
class Parents(models.Model):
    username = models.CharField(max_length=250)
    phone = models.IntegerField(max_length=200)
    email = models.EmailField(max_length=255)
    student_name = models.ForeignKey(Student , on_delete=models.PROTECT)

