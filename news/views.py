from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class AuthorList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Author
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'rate'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'authors.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'authors'
# Create your views here.


class PostList(ListView):
    model = Post
    ordering = 'time_post'
    template_name = 'start.html'
    context_object_name = 'posts'


class PostAll(ListView):
    model = Post
    ordering = 'time_post'
    template_name = 'posts.html'
    context_object_name = 'allposts'


class NewsN(DetailView):
    model = Post
    template_name = 'newsn.html'
    context_object_name = 'newsn'
