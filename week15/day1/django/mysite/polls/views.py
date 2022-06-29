from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  # pass view information into the browser

# takes a request, returns a response


def index(request):
    user = {
        'first_name': "John",
        'last_name': "Doe"
    }

    subjects = [
        {
            'title': "How to setup Django",
            'author': "Maria"
        },
        {
            'title': "How to cake an amazing pie",
            'author': "Chef Mark"
        }
    ]

    context = {
        'user': user,
        'subjects': subjects
    }
    return render(request, "post/homepage.html", context)


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    return render(request, "index.html", {})


def about(request):
    return HttpResponse('<h1> Sort de mon coeur !!! </h1>')
