from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime
from .filters import PostFilter


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
    paginate_by = 2  # вот так мы можем указать количество записей на странице


class PostAll(ListView):
    model = Post
    ordering = 'time_post'
    template_name = 'posts.html'
    context_object_name = 'allposts'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['new_post'] = "Свежие новости сегодня!"
        context['filterset'] = self.filterset
        return context


class NewsN(DetailView):
    model = Post
    template_name = 'newsn.html'
    context_object_name = 'newsn'
