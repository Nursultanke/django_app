from django.urls import path
from .views import index, my_list, about

urlpatterns = [
    path('', index),
    path('list/', my_list),
    path('about', about, kwargs={"name":"Tom", "age": 38}),
]