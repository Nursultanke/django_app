from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Список продукт'

