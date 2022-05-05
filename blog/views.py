from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    category = Category_post.objects.all()
    photo = Photo.objects.all()
    context = {'post': post,
               'category': category,
               'photo': photo, }
    return render(request, 'blog/post_detail.html', context=context)


def category_list(request, category_slug):
    category = get_object_or_404(Category_post, slug=category_slug)
    context = {'category': category}
    return render(request, 'blog/list_categories.html', context=context)



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
    category = Category_post.objects.all()
    context = {
        'posts': posts,
        'category':category
    }
    return render(request, 'blog/show_news.html', context)














