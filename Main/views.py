from django.shortcuts import render
from .models import AboutMe


def home(request):
    AboutMe.objects.get(name='Ryan')

    context = {}

    return render(request, 'main/home.html', context=context)
