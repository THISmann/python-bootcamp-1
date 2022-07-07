from django.db import models
from datetime import datetime,date

class Student(models.Model):
    username = models.CharField(max_length=50)
    classe = models.CharField(max_length=50) # one to many relationship
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50) # one to many 
    phone_number = models.IntegerField(max_length=255)
    
class Teacher(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50) # one to many 
    suject = models.CharField(max_length=30)
    phone_number = models.IntegerField(max_length=255)
    
class Parent(models.Model):
    username = models.CharField(max_length=50)
    Student_id = models.CharField(max_length=50) # one to many relationship
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=255) 
    

# Create your models here.
