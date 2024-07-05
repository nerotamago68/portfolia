from django.shortcuts import render
from .models import AboutMe


def home(request):
    about = AboutMe.objects.get(name='Ryan')

    context = {
        'about': about
    }

    return render(request, 'main/home.html', context=context)
