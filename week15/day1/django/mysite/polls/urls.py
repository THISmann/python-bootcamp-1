from django.urls import path  # path function
from . import views  # . is shorthand for the current directory


# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
    # path('about_website/', views.about, name='about'),
]


# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route
