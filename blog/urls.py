from django.urls import path
from . import views
from .views import (
    HomeListView,
    PostsByCategoryListView,
    PostDetailView,
    CreatePostView,
    CategoryDetailView
)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:category_slug>/', cache_page(30)(PostsByCategoryListView.as_view()), name='category'),
    path('add/', CreatePostView.as_view(), name='add_post'),
    path('category/detail/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('register/', views.register, name='register'),
]