from django.urls import path
from .views import *

urlpatterns = [
    path('', show_news, name='news'),
    path('/<int:pk>/', post_detail, name='post_detail'),


]
