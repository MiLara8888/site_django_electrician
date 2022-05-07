from django.urls import path
from .views import *

urlpatterns = [
    path('', PriceTable.as_view(), name='price_table'),
    path('search/', search, name='search'),
]
