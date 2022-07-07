from django.db import models
from datetime import datetime,date

class Presence(models.Model):
    student_name = models.CharField(max_length=50)  # one to many relationship
    matiere = models.CharField(max_length=50)   
    prof_name = models.EmailField(max_length=50)   
    