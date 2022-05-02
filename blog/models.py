from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=200, verbose_name='Заголовок')
    header2 = models.CharField(max_length=250, verbose_name='Подзаголовок', blank=True)
    text = models.TextField(verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image_preview = models.ImageField(upload_to='photo_preview/%Y/%m/%d/',verbose_name='Главное фото')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Блог/статья'
        verbose_name_plural = 'Блоги/статьи'


class Photo(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/',verbose_name='Фото',blank=True)
    product=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='Статья в которой фото')




    class Meta:
        verbose_name='Фото'
        verbose_name_plural = 'Фото'
