from django.shortcuts import render
from django.http import HttpResponse

import random


def home(request):
    return render(request, 'passwordapp/home.html')


def pwd(request):

    characters = list('abcdefghijklmnopqrstuvwxy')

   

    if request.GET.get('Numbers'):
        characters.extend(list('0987654321'))
        
    if request.GET.get('UpperCase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   
    if request.GET.get('characters'):
        characters.extend(list('!@£$%^&*'))                

    length = int(request.GET.get('length', 7))

    thepasssword = ''
    for x in range(length):
        thepasssword += random.choice(characters)

    return render(request, 'passwordapp/pwd.html', {'pwd':thepasssword})  