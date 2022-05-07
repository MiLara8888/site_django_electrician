from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    desc=post.category_post
    category_list = Category_post.objects.all().order_by('name_category')
    photo = Photo.objects.all()
    context = {'post': post,
               'photo': photo,
               'category_list': category_list,
               'desc':desc,}
    return render(request, 'blog/post_detail.html', context=context)

def category_list(request, category_slug=None):
    category = None
    posts = Post.objects.all().order_by('-time_create')
    if category_slug:
        category = get_object_or_404(Category_post, slug=category_slug)
        posts = posts.filter(category_post=category)
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
    category_list = Category_post.objects.all().order_by('name_category')
    context = {
        'posts': posts,
        'category': category,
        'category_list': category_list
    }
    return render(request, 'blog/show_news.html', context)


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
    category_list = Category_post.objects.all().order_by('name_category')
    context = {
        'posts': posts,
        'category_list': category_list
    }
    return render(request, 'blog/show_news.html', context)



