from django.shortcuts import render, redirect
from .models import Products, Bycycle, Watches


def index(request):
    datas = Products.objects.all()
    return render(request, 'pages/first_page.html', {'data': datas})


def second_page(request):
    return render(request, 'pages/second.html')


def bicycle_page(request):
    bicycle = Bycycle.objects.all()
    return render(request, 'pages/bycycle_page.html', {'bicycle': bicycle})


def watch_page(request):
    watch = Watches.objects.all()
    return render(request, 'pages/watch_page.html', {'watch': watch})


def bio(request):
    return render(request, 'pages/bio.html')


def create_products(request):
    if request.method == "GET":
        return render(request, 'pages/create_product.html')

    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['desc']

        products = Products(name=name, price=price, description=description)
        products.img = request.FILES.get('image')
        products.save()

        return redirect('index')