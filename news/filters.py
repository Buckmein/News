from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Post, Category

# Создаем свой набор фильтров для модели Posts.
# FilterSet, который мы наследуем,


class PostFilter(FilterSet):
    category = ModelChoiceFilter(field_name='postcategory__category',
queryset=Category.objects.all(),
label='Категория',
empty_label='Любая')


    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск заголовку
           'title': ['icontains'],
           # поиск автору
           #'author': ['icontains'],
           # поиск категории
           # рейтинг должен быть больше или равен
           'rate': ['gt'],
           #'time_post': [
           #    'lt',  # дата должна быть меньше или равна указанной
            #    'gt',  # дата должна быть больше или равна указанной
           #],
       }
