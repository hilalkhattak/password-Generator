from django.shortcuts import render
from django.http import HttpResponse

import random


def home(request):
    return render(request, 'passwordapp/home.html')

def pwd(request):

    

    characters = list('abcdefghijklmnopqrstuvwxy')

    length = int(request.GET.get('length'))

    thepasssword = ''
    for x in range(length):
        thepasssword += random.choice(characters)

    return render(request, 'passwordapp/pwd.html', {'pwd':thepasssword})  