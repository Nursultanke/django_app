from django.shortcuts import render
from django.http import HttpResponse


def contacts(request):
    return HttpResponse('<h1>Contacts page</h1>')

