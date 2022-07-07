from django.db import models
from datetime import datetime,date

class Devoir(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50) # one to many relationship
    description = models.EmailField(max_length=50) 
    prof_name = models.CharField(max_length=50) # one to many 
    classe = models.CharField(max_length=50) # one to many 
    date_start = models.DateField()
    date_end = models.DateField()