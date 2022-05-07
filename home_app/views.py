from django.shortcuts import render
from .models import *

def home(request):
    carousel=Carousel.objects.all()
    c1=carousel[0]
    car=carousel[1:]
    circle=Circle.objects.all()

    big_im=BigImage.objects.all()
    context={
        'car':car,
        'c1':c1,
        'circle':circle,
        'big_im':big_im,
    }
    return render(request, 'home_app/home.html',context=context)