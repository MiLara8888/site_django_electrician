from django.urls import path
from .views import *

urlpatterns = [
    path('', show_news, name='news'),
    path('<slug:post_slug>/', post_detail, name='post_detail'),
    path('<slug:category_slug>/',category_list , name='category_url'),


]
