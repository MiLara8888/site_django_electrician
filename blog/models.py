from django.db import models
from django.urls import reverse


class Post(models.Model):
    header = models.CharField(max_length=200, verbose_name='Заголовок')
    header2 = models.CharField(max_length=250, verbose_name='Подзаголовок', blank=True)
    text = models.TextField(verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image_preview = models.ImageField(upload_to='photo_preview/%Y/%m/%d/', verbose_name='Главное фото')
    category_post = models.ForeignKey('Category_post', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Категория статьи')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL Поста')

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_slug': self.slug})   #1 передаем имя из urla в kwargs передаем имя

    class Meta:
        verbose_name = 'Глерея работ/статья'
        verbose_name_plural = 'Галерея работ/статьи'


class Photo(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото статьи', blank=True)
    product = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья в которую фото')
    description_photo = models.CharField(max_length=250, verbose_name='Описание фото (необязательно)', blank=True)

    class Meta:
        verbose_name = 'Добавить фото'
        verbose_name_plural = 'Добавить фотографии к статьям'


class Category_post(models.Model):
    name_category = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL категории')  # Человеко понятный url
    description=models.CharField(max_length=250, verbose_name='Подзаголовок пара слов о категории (Необязательно)', blank=True)

    def get_absolute_url(self):  # Создание персональной ссылки для обекта
        return reverse('category_url', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Добавить категории к статьям'
        verbose_name_plural = 'Добавить категории к статьям'
