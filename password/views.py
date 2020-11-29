from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'passwordapp/home.html')

def phones(request):
    return HttpResponse('phones from where to choose')    