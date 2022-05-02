from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def show_news(request):
#     posts = Post.objects.all().order_by('-time_create')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/show_news.html', context=context)

def show_news(request):
    posts = Post.objects.all().order_by('-time_create')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'blog/show_news.html', context)





