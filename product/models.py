from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name
# варианты on_delete
# CASCADE - при удалении категории, ядалятся все продукты с этой категориии
# SET_NULL - при удалении категории, значеник поля Category для связанных продуктов станет пустым
# SET_DEFAULT - при удалении категории, значение поля Category в связанных продуктах заменяется на дефолтное
# PROTECTED - не дает удалить категорию, если в ней есть продукты
# RESTRICT - не дает удалить категорию, если в ней есть продукты
# NO_NOTHING - ничего не делает


class Product(models.Model):
    title = models.CharField(max_length=100)
    descripiton = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', null=True, blank=True)


# ORM (Object-Relation Mapping)
# связывает классы в каком-то языке и таблицы в базе данных

