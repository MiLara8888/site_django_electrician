from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

def home(request):
    return render(request, 'electric_app/home.html')



# def price_table(request):
#     category=Category.objects.all()
#     list_price=Price.objects.all()
#     return render(request, 'electric_app/price_table.html',{'category':category,'list_price':list_price})

class PriceTable(TemplateView):       #для вывода таблиц
    template_name = 'electric_app/price_table.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context



