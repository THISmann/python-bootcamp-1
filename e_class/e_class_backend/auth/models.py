from django.db import models
from datetime import datetime,date

class Students(models.Model):
    username = models.CharField(max_length=50)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    school_name = models.ForeignKey(SchoolName, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=255) 
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.username
    
    
class Teachers(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    school_name = models.ForeignKey(SchoolName, on_delete=models.CASCADE)
    suject = models.ForeignKey(Topics, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=255)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.username
    
class Parents(models.Model):
    username = models.CharField(max_length=50)
    Student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=255)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.username
    
#class Topics(models.Model)
class Topics(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.title
   
class SchoolName(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.name
    
class Classe(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.name

# Create your models here.
