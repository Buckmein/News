from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateFilter
from django.forms import DateInput
from .models import Post, Category

# Создаем свой набор фильтров для модели Posts.
# FilterSet, который мы наследуем,


class PostFilter(FilterSet):

    date = DateFilter(field_name='time_post',
                      widget=DateInput(attrs={'type': 'date'}),
                      label='Не раньше:',
                      lookup_expr='date__gte'
                      )

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
           'author__user': ['exact'],
           # поиск категории
           # рейтинг должен быть больше или равен
           'rate': ['gt'],
       }
