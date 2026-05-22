from django import template
from blog.models import Category

register = template.Library()


#  ПРОСТОЙ ТЕГ
@register.simple_tag(name='get_categories')
def get_categories():
    """Возвращает все категории"""
    return Category.objects.all()


#  ТЕГ ВКЛЮЧЕНИЯ
@register.inclusion_tag('blog/list_categories.html')
def show_categories(arg=None):
    """
    Возвращает категории и рендерит их в шаблон.
    arg - дополнительный аргумент (например, для выбора активной категории)
    """
    categories = Category.objects.all()
    return {
        'categories': categories,
        'arg': arg,  # передаём аргумент в шаблон
    }