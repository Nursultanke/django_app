from django.urls import path
from .views import index, second_page, bicycle_page, watch_page

urlpatterns = [
    path('', index, name='index'),
    path('second_page/', second_page, name='second_page'),
    path('bicycle_page/', bicycle_page, name='bicycle_page'),
    path('watch_page/', watch_page, name='watch_page'),
]