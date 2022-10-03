from django.urls import path
from .views import index, second_page, bicycle_page

urlpatterns = [
    path('', index),
    path('second_page/', second_page),
    path('bicycle_page/', bicycle_page)
]