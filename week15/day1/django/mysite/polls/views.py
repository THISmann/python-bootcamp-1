from .forms import ContactForm
from django.shortcuts import render
from .models import Person, Post  # import the models from polls/models.py
from rest_framework import viewsets          # add this
from rest_framework.serializers import *     # add this
from .models import Task
from .serialazers import *
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class TasksView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class PostsView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


person = Person.objects.filter(first_name="Maria",
                               last_name="Fez").first()
# get the first object because Person.objects.filter returns a QuerSet (ie. a list)


def index(request):
    context = {
        'page_title': "Homepage",
        'user': person
    }
    return render(request, 'post/homepage.html', context)


def posts(request):
    context = {
        'page_title': "Posts",
        'posts': Post.objects.filter(
            author__first_name=person.first_name,
            author__last_name=person.last_name)
    }
    return render(request, 'post/posts.html', context)


def home(request):
    return "welcome to the home page !!! "


def contact(request):
    context = {
        'page_title': "Contact",
        'user': person,
        'form': ContactForm()

    }
    # if the submit button was clicked
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            form_name = form['name'].value
            form_email = form['email'].value
            form_comment = form['comment'].value
            context['formInfo'] = [form_name, form_email, form_comment]
            # render to a the same url, but with new data:
            return render(request, 'post/contact.html', context)
    else:
        # GET, generate blank form
        context['form'] = ContactForm()
    return render(request, 'post/contact.html', context)
