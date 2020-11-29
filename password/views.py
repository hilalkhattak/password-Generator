from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'passwordapp/home.html')

def pwd(request):
    return render(request, 'passwordapp/pwd.html')  