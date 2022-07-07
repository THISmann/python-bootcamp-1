from django.db import models
from datetime import datetime,date

class Forum(models.Model):
    username = models.CharField(max_length=50)  # one to many relationship
    title = models.CharField(max_length=50)   
    message = models.EmailField(max_length=50)  