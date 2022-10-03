from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = list_display


admin.site.register(Products, ProductsAdmin)
