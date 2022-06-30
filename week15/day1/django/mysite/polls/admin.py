# Register your models here.
from django.contrib import admin
from .models import *  # import the Person model

# Register your models here.
admin.site.register(Person)
admin.site.register(Task)
admin.site.register(Post)
