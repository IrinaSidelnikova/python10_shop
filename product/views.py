# Импорт их страндартной библиотеки Python
# 2 Импорт из строронних библиотек(что устанавливаем черех pip: django, bs4)
# 3 Импорты из самого проекта
import django_filters
from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Category, Product


class IndexPageView(ListView):
    model = Category
    template_name = 'product/index.html'
    context_object_name = 'categories'

# queryset (список объектов данного класса) результат = [category1, category2, category3]
# обработчик запроса, представление (view)


class ProductFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter('price', 'gte')
    price_to = django_filters.NumberFilter('price', 'lte')

    class Meta:
        model = Product
        fields = ['price_from', 'price_to']

# products/category_slug/


class ProductsListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 4
    filterset_class = ProductFilter
    # 'products/category/?page=2'
    # product/category?price_from=1000&price_to=2000

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        queryset = super().get_queryset()
        # queryset -> Product.objects.all()
        queryset = queryset.filter(category_id=category_slug)

        # # фильтрация по стоимости
        queryset = ProductFilter(self.request.GET, queryset=queryset).qs

        # сортировка
        # products/category/?sort=price_asc
        sort = self.request.GET.get('sort')
        sort_choices= {'price_asc': 'price',
                       'price_desc': '-price',
                       'title_asc':'title',
                       'title_desc': '-title'}
        sort = sort_choices.get(sort)
        if sort:
            queryset = queryset.order_by(sort)
        # Product.objects.all().filter()
        return queryset


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'


# <p><a href="{% url 'products-list' cat.slug %}">{{cat.name}}</a></p>
# <p><a href="{% url 'products-list' %}?category={{ cat.slug }}">{{cat.name}}</a></p>