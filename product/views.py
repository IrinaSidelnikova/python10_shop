from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView

from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})


def product_list(request):
    products = Product.objects.all()
    # objects - страндартный менеджер модели
    # Product.objects.all() == SELECT * FROM Product;
    return render(request, 'product/products_list.html', {'products': products})

    # queryset (список объектов данного класса) результат = [category1, category2, category3]
# обработчик запроса, представление (view)
# product/category
def products_list(request, category_slug):
    products = Product.objects.filter(category_id=category_slug)
    # SELECT * FROM product WHERE category_id=category_slug
    return render(request, 'product/products_list.html', {'products': products})

# products/?category=... - параметр запроса
# def products_list(request):
#     products = Product.objects.all()
#     category_slug = request.GET.get('category')
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     # products = Product.objects.filter(category_id=category_slug)
#     return render(request, 'product/products_list.html', {'products': products})


def products_list(request, category_slug):
   products = Product.objects.filter(category_id=category_slug)
   return render(request, 'product/products_list.html', {'products': products})

# 1 вариант
# products/id
def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    # product = Product.objects.get(id=id)
    # SELECT * FROM product WHERE id=id LIMIT 1;
    return render(request, 'product/product_details.html', {'product':product})
# 2 вариант
class ProductDetails(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return render(request, 'product/product_details.html', {'product': product})
# 3 вариант
class ProductDetails(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'


# <p><a href="{% url 'products-list' cat.slug %}">{{cat.name}}</a></p>
# <p><a href="{% url 'products-list' %}?category={{ cat.slug }}">{{cat.name}}</a></p>