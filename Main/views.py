from django.shortcuts import render
from .models import AboutMe


def home(request):
    

    context = {
        'about': 'sdsdsd'
    }

    return render(request, 'main/home.html', context=context)
