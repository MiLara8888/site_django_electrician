from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('price_table/',PriceTable.as_view(),name='price_table'),
]