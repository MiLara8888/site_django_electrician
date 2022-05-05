from django.urls import path
from .views import *

urlpatterns = [
    path('', show_news, name='news'),
    path('<slug:category_slug>/', category_list, name='category_url'),
    path('post/<slug:post_slug>/', post_detail, name='post_detail'),

]
