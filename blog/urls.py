from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.posts_by_category, name='category'),
]