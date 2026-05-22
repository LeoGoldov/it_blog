from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    """Главная страница со списком всех постов"""
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'title': 'Главная'
    })

def post_detail(request, post_id):
    """Страница отдельного поста"""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'title': post.title
    })

def posts_by_category(request, category_slug):
    """Страница с постами определённой категории"""
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category.html', {
        'posts': posts,
        'category': category,
        'title': category.name
    })