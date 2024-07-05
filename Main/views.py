from django.shortcuts import render
from .models import AboutMe


def home(request):

    context = {}

    return render(request, 'main/home.html', context=context)
