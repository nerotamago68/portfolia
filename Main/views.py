from django.shortcuts import render
from .models import AboutMe

# Create your views here.


def home(request):
    about_me = AboutMe.objects.get(name='Ryan')

    context = {
        'about': about_me,
    }

    return render(request, 'main/home.html', context=context)
