from django.contrib import admin
from .models import Products, Bycycle


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = list_display


class BycycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'b_mark', 'b_model')
    list_display_links = list_display


admin.site.register(Products, ProductsAdmin)
admin.site.register(Bycycle, BycycleAdmin)
