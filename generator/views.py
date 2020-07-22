from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def Jason(request):
    return HttpResponse('<h1>Jason is the Boss</h1>')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters += [str(i).upper() for i in characters]

    if request.GET.get('numbers'):
        characters.extend([str(i) for i in range(10)])

    if request.GET.get('special'):
        characters.extend(['!@#$%^&*()'])

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request,'generator/about.html')

def pinyin(request):
    return render(request, 'generator/pinyin.html')