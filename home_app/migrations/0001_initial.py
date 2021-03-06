# Generated by Django 4.0.4 on 2022-05-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField(default=True, verbose_name='Картинка справа')),
                ('image_big', models.ImageField(upload_to='photo_big/%Y/%m/%d/', verbose_name='Большая картинка на главной')),
                ('header_big', models.CharField(max_length=150, verbose_name='Заголовок около большой картинки')),
                ('header2_big', models.CharField(max_length=350, verbose_name='Подзаголовок около большой картинки')),
            ],
            options={
                'verbose_name': 'Записи с большой картинкой на главной',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_car', models.CharField(blank=True, max_length=100, verbose_name='Заголовок карусели')),
                ('header2_car', models.CharField(blank=True, max_length=150, verbose_name='Подзаголовок карусели')),
                ('image_car', models.ImageField(upload_to='photo_car/%Y/%m/%d/', verbose_name='Картинка в карусели')),
            ],
            options={
                'verbose_name': 'Карусель на главной',
            },
        ),
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_circle', models.CharField(max_length=80, verbose_name='Заголовок кругляшка')),
                ('header2_circle', models.CharField(max_length=150, verbose_name='Подзаголовок круглого')),
                ('image_circle', models.ImageField(upload_to='photo_circle/%Y/%m/%d/', verbose_name='Картинка в кругляшке')),
            ],
            options={
                'verbose_name': 'Круги на главной',
            },
        ),
    ]
