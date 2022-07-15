from django.db import models
from datetime import datetime , date 

class Discipline(models.Model):
    #student_name = models.ForeignKey(to=Student , on_delete=)
    school_years = models.DateField()
    
# Create your models here.
