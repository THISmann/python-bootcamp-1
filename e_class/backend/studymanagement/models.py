from django.db import models
from datetime import datetime, date

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    #classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone_numero = models.IntegerField()
    #etablissement = models.ForeignKey(Etablissement)
