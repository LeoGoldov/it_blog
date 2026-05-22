from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    """Модель для категорий"""
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('URL-метка', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Возвращает URL на страницу категории"""
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # если категорию удалим, у поста будет null
        null=True,
        blank=True,
        verbose_name='Категория',
        related_name='posts'

    )

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']