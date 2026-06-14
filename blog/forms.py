from django import forms
from .models import Category, Post
import re
from django.core.exceptions import ValidationError


def validate_title_not_start_with_digit(value):
    """Проверяет, что заголовок не начинается с цифры"""
    if value and value[0].isdigit():
        raise ValidationError('Заголовок не может начинаться с цифры!')


from .models import Category

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    captcha = CaptchaField(label='Капча')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выберите категорию',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class PostModelForm(forms.ModelForm):
    """Связанная форма для модели Post"""
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  # явно указываем поля (не '__all__'!)
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'category': 'Категория',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }