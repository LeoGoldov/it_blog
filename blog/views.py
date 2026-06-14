from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostModelForm
from django.shortcuts import redirect

# ========== ListView для главной страницы ==========
class HomeListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().select_related('category')  # .filter(is_published=True) если есть такое поле


#def posts_by_category(request, category_slug):
   # category = get_object_or_404(Category, slug=category_slug)
    #posts = Post.objects.filter(category=category)
    #return render(request, 'blog/category.html', {'posts': posts, 'category': category})
#Класс для категорий
class PostsByCategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Фильтруем посты по slug категории"""
        self.category = Category.objects.get(slug=self.kwargs['category_slug'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['title'] = self.category.name
        return context


# ========== DetailView для отдельного поста ==========
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'  # чтобы работал post_id вместо pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


# CreateView для добавления поста ==========
class CreatePostView(CreateView):
    form_class = PostModelForm  # или NewsForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')  # временно, потом переопределим

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление поста'
        return context

    def form_valid(self, form):
        """После сохранения редиректим на страницу созданного поста"""
        self.object = form.save()
        return redirect('post_detail', post_id=self.object.id)


#  ИНД задание
# DetailView для модели Category
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'  # используем slug вместо pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.object.name}'
        context['posts'] = Post.objects.filter(category=self.object)
        return context