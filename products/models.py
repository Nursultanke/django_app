from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    price = models.FloatField(verbose_name='Цена')
    img = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Список продукт'


class Bycycle(models.Model):
    b_mark = models.CharField(max_length=20, verbose_name='марка')
    b_model = models.CharField(max_length=30, verbose_name='модель')
    price = models.FloatField(verbose_name='цена')
    b_color = models.CharField(max_length=20, verbose_name='цвет')

    def __str__(self):
        return self.b_mark

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Список велосипедов'


class Watches(models.Model):
    w_mark = models.CharField(max_length=20, verbose_name='название')
    price = models.FloatField(verbose_name='цена')
    color = models.CharField(max_length=20, verbose_name='цвет')
    made_in = models.CharField(max_length=30, verbose_name='сделано в')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.w_mark

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Список часов'
