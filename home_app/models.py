from django.db import models


class Carousel(models.Model):
    header_car = models.CharField(max_length=100, verbose_name='Заголовок карусели', blank=True)
    header2_car = models.CharField(max_length=150, verbose_name='Подзаголовок карусели', blank=True)
    image_car = models.ImageField(upload_to='photo_car/%Y/%m/%d/', verbose_name='Картинка в карусели')

    def __str__(self):
        return self.header_car

    class Meta:
        verbose_name = 'Карусель на главной'
        verbose_name_plural='Карусель на главной'



class Circle(models.Model):
    header_circle = models.CharField(max_length=80, verbose_name='Заголовок кругляшка')
    header2_circle = models.CharField(max_length=150, verbose_name='Подзаголовок круглого')
    image_circle = models.ImageField(upload_to='photo_circle/%Y/%m/%d/', verbose_name='Картинка в кругляшке (Обязательно квадратная)')

    def __str__(self):
        return self.header_circle

    class Meta:
        verbose_name = 'Круги на главной'
        verbose_name_plural = 'Круги на главной'


class BigImage(models.Model):
    is_right = models.BooleanField(default=True, verbose_name='Картинка справа')
    image_big = models.ImageField(upload_to='photo_big/%Y/%m/%d/', verbose_name='Большая картинка на главной (Обязательно квадратная)')
    header_big = models.CharField(max_length=150, verbose_name='Заголовок около большой картинки')
    header2_big = models.CharField(max_length=350, verbose_name='Подзаголовок около большой картинки')

    def __str__(self):
        return self.header_big

    class Meta:
        verbose_name = 'Записи с большой картинкой на главной'
        verbose_name_plural = 'Записи с большой картинкой на главной'
