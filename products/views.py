from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    datas = [{'deal': 'Action deal 1',
            'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
            'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Action deal 2',
             'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
             'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Action deal 3',
             'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
             'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Action deal 4',
             'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
             'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Action deal 5',
             'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
             'cash_back': 'buy 3 and get 1 free'},
            {'deal': 'Action deal',
             'img': 'https://img.freepik.com/premium-photo/beautiful-asian-woman-carrying-colorful-bags-shopping-online-with-mobile-phone_8087-3877.jpg?w=2000',
             'cash_back': 'buy 3 and get 1 free'},

            ]

    return render(request, 'main.html', {'data': datas})


def my_list(request):
    return HttpResponse("<h1>Title</h1>")


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)