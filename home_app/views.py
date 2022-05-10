from django.shortcuts import render
from .models import *



def home(request):
    carousel = Carousel.objects.all()
    circle = Circle.objects.all()
    big_im = BigImage.objects.all()
    context = {
        'car': carousel,
        'circle': circle,
        'big_im': big_im,
    }
    return render(request, 'home_app/home.html', context=context)