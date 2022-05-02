# Generated by Django 4.0.4 on 2022-04-29 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Катерия')),
            ],
            options={
                'verbose_name': 'Катерия',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование услуги')),
                ('unit', models.CharField(max_length=30, verbose_name='Единица измерения')),
                ('price', models.CharField(max_length=40, verbose_name='Цена')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electric_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]
