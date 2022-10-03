from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Bycycle


def index(request):
    datas = Products.objects.all()
    return render(request, 'pages/first_page.html', {'data': datas})


def second_page(request):
    return render(request, 'pages/second.html')


def bicycle_page(request):
    bicycle = Bycycle.objects.all()
    return render(request, 'pages/bycycle_page.html', {'bicycle': bicycle})
