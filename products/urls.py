from django.urls import path
from .views import index, second_page

urlpatterns = [
    path('', index),
    path('second_page/', second_page)
]