from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostAll.as_view(), name='post_list'),
   path('author/', AuthorList.as_view()),
   path('post/<int:pk>', NewsN.as_view(), name='post_detail'),
   path('article/create/', ArticleCreate.as_view(), name='art_create'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='att_update'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='art_delete'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]