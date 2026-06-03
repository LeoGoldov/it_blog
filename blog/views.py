from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import NewsForm, PostModelForm
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


from .forms import NewsForm, PostModelForm

from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import Post


def add_post(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Post.objects.create(  # ← сохраняем post в переменную
                title=cd['title'],
                content=cd['content'],
                category=cd['category']
            )
            return redirect('post_detail', post_id=post.id)  # ← редирект на созданный пост
    else:
        form = NewsForm()

    return render(request, 'blog/add_post.html', {'form': form})