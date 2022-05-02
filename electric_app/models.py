from django.db import models


class Price(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование услуги')
    unit = models.CharField(max_length=30, verbose_name='Единица измерения')
    price = models.CharField(max_length=40, verbose_name='Цена')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

