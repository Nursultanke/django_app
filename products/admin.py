from django.contrib import admin
from .models import Products, Bycycle, Watches


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = list_display


class BycycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'b_mark', 'b_model')
    list_display_links = list_display


class WatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'w_mark', 'price')
    list_display_links = ('w_mark',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Bycycle, BycycleAdmin)
admin.site.register(Watches, WatchAdmin)
