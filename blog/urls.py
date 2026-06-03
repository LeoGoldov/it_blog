from django.urls import path
from . import views
from .views import (
    HomeListView,
    PostsByCategoryListView,
    PostDetailView,
    CreatePostView,
    CategoryDetailView  # для индивидуального задания
)

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:category_slug>/', PostsByCategoryListView.as_view(), name='category'),
    path('add/', CreatePostView.as_view(), name='add_post'),
    path('category/detail/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
]