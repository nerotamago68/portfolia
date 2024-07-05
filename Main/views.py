from django.shortcuts import render
from .models import AboutMe

# Create your views here.


def home(request):


    context = {}

    return render(request, 'main/home.html', context=context)
