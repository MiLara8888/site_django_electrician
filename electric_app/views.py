from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic import TemplateView
from django.db.models import Q


class PriceTable(TemplateView):

    template_name = 'electric_app/price_table.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search', '').lower()

        if query == '':
            query = 'None'


    results = Price.objects.filter(Q(title__icontains=query) | Q(title__icontains=query.capitalize()))
    results2 = Category.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()))
    return render(request, 'electric_app/search_table.html', {'query': query, 'results': results, 'results2': results2})
