#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#TODO: Заполнит товары
#TODO Сделать список товаров на сайте
#TODO: Добавить возможность загружать картинки товаров

# Product.objects.all()
# SELECT * FROM product

# .filter(условие) - выдает результаты, отвечающие условиям
# Product.objects.filter(price__gt=100)
# SELECT * FROM product WHERE price > 100 условия;

# .exclude(условия) - исключает результаты, отвечающие условиям
# Product.objects.exclude(price__gt=100)
# SELECT * FROM product WHERE NOT price > 100;
#
# .get(условия) - получает один конкретный объект
# Product.objects.get(id=2)
# SELECT * FROM product WHERE id=2;
#
# # Если по запросу не найдено ни одной записи
# # DoesNotExist
#
# # Если найдено более одной записи
# # MultipleObjectsReturned
#
# # .create() - метод, для создания объектов модели
# #     Category.objects.create(name='Аксессуары', slug='accessories')
# #     INSERT INTO product VALUES ('Аксессуары', 'accessories');
#
#
# # cat1 = Category(name='Аксессуары', slug='accessories')
# # cat1.save()
#
# # .update() - обновление объектов
# # Можно применять ко всем записям, можно по отдельности
# # Product.objects.update() - для всех
# # Product.objects.filter(...).update(...)- только для определенных записей
#
# # Product.object.filter(category_id='notebooks').update(price=F('price') - 1000)
# # UPDATE product SET price = price - 1000 WHERE category_id = 'notebooks';
#
# .defer()
# .only()
#
# # title, description, price, category_id
#     # Product.oblects.all()
#     # SELECT title,  description, price, category_id FROM product;
#
# title, price
#     # Product.objects.only('title', 'price')
#     # Product.objects.defer('description', 'category_id')
#     # SELECT title, price FROM product;
#
# # .order_by()
# #     Product.objects.order_by('price')
# #     SELECT * FROM product ORDER BY price ASC;
# #
# #     Product.objects.order_by('-price')
# #     SELECT * FROM product ORDER BY price DESC;
# .all()
# Product.objects.all()
# <QuerySet[obj1, obj2, obj3, ...]>
#
# # .values() - выдает записи в виде словаря
# Product.objects.values
# <QuerySet[{'id':1, 'title':'Apple Iphone', 'description':...},
#             {'id':2, 'title':'Redmi', 'description':...}, ...]
#
# Product.objects.values('title', 'price')
# <QuerySet[
#     {'title':'aasgv', 'price':210.00},
#     {'title': 'bbbb', 'price':280.00}]>
#
#
# .values_list()
# Products.objects.values_list()
# <QuerySet[('Apple Iphone 12', 'Lorem Ipsum', 200.00, ...),
#           ('Redmi Note 9', 'Dolor Sit amet', 250.00, ...)]>
#
# Products.objects.values_list('title', 'price')
# <QuerySet[('Apple Iphone 12', 200.00, ...),
#           ('Redmi Note 9', 250.00, ...)]>
#
# Product.objects.values_list('title')
# <QuerySet[('Apple Iphone 12',...),
#           ('Redmi Note 9',...),
#           ('Xiaomi Mi 10', ...)]>
#
# Product.object.values_list('title', flat=True)
# <QuerySet['Apple Iphone 12', 'Redmi Note 9', 'Xiaomi Mi 10', ...]>
#
# # .count() - возвращает кол-во результатов запроса
# # Product.objects.all.count()
# # Product.objects.count()
# # SELECT COUNT(*) FROM product;
#
# # Product.oblects.filter(...).count()
# # SELECT COUNT(*) FROM product WHERE ...;
#
# # .first() - возвращает первый объект из результата запроса
# # .last() - возвращает последний объект
#
# # Если нет ни одной записи в результате возвращается None
#
# # .exists() - проверяет, есть ли в результатах запроса хотя бы одна запись
# # Применяется вместе с фильтрациией
#
# # Выборки по полям
# # __gt -> '>'
# # __lt -> "<"
# # __gte -> ">="
# # __lte -> "<="
#
# Product.objects.filter(price__gt=20000)
# SELECT * FROM product WHERE price >=20000;
#
# Product.objects.filter(price=20000)
# SELECT * FROM product WHERE price=20000;
#
# # __range -> BETWEEN
#
# # Product.objects.filter(price__gte=20000, price__lte=50000)
# # SELECT * FROM product WHERE price >= 20000 AND price <= 50000;
# #
# # Product.objects.filter(price__range=(20000, 50000))
# # SELECT * FROM product WHERE price BETWEEN 20000 AND 50000;
#
# # exact
# # iexact
#
# # Product.objects.filter('title__exact'='Apple')
# # SELECT * FROM product WHERE title = 'Apple'
# #
# # Product.objects.filter(title__iexact='Apple')
# # SELECT * FROM product WHERE title ILIKE 'Apple'
#
# # stastswith
# # isstartswith
# Product.objects.filter(title__starswith='Apple')
# # SELECT * FROM product WHERE title LIKE 'Apple%';
# Product.objects.filter(title__isstarswith='Apple')
# # SELECT * FROM product WHERE title ILIKE 'Apple%';
#
# # endswith
# # iendswith
# Product.objects.filter(title__endswith='Apple')
# # SELECT * FROM product WHERE title LIKE '%Apple';
# Product.objects.filter(title__iendswith='Apple')
# # SELECT * FROM product WHERE title ILIKE '%Apple';
#
# # contains
# # icontains
# Product.objects.filter(title__contains='Apple')
# # SELECT * FROM product WHERE title LIKE '%Apple%';
# Product.objects.filter(title__icontains='Apple')
# # SELECT * FROM product WHERE title ILIKE '%Apple%';
#
# # in - проверка на вхождение в список
# Product.objects.filter(category_id__in=['notebooks', 'cellphones'])
# # SELECT * FROM product WHERE category_id in ('notebooks', 'cellphones'));
#
# # isnull
# Product.objects.filter(image__isnull=True)
# # SELECT * FROM product WHERE image IS NULL;
#
# Product.objects.filter(image__isnull=False)
# # SELECT * FROM product WHERE image IS NOT NULL;
#
# # date
# Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
# Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))
#
# # year
# Entry.objects.filter(pub_date__year=2005)
# # SELECT ... WHERE pub_date BETWEEN '2005-01-01' AND '2005-12-31';
# Entry.objects.filter(pub_date__year__gte=2005)
# # SELECT ... WHERE pub_date >= '2005-01-01';
#
# # iso_year
# Entry.objects.filter(pub_date__iso_year=2005)
# Entry.objects.filter(pub_date__iso_year__gte=2005)
#
# # month
# Entry.objects.filter(pub_date__month=12)
# # SELECT ... WHERE EXTRACT('month' FROM pub_date) = '12';
# Entry.objects.filter(pub_date__month__gte=6)
# # SELECT ... WHERE EXTRACT('month' FROM pub_date) >= '6';
#
# # day
# Entry.objects.filter(pub_date__day=3)
# # SELECT ... WHERE EXTRACT('day' FROM pub_date) = '3';
# Entry.objects.filter(pub_date__day__gte=3)
# # SELECT ... WHERE EXTRACT('day' FROM pub_date) >= '3';
#
# # week
# Entry.objects.filter(pub_date__week=52)
# Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)
#
# # week_day - определяет день недели
# Entry.objects.filter(pub_date__week_day=2)
# Entry.objects.filter(pub_date__week_day__gte=2)
#
# # iso_week_day
# Entry.objects.filter(pub_date__iso_week_day=1)
# Entry.objects.filter(pub_date__iso_week_day__gte=1)
#
# # quarter - квартал года
# Entry.objects.filter(pub_date__quarter=2)
#
# # time
# Entry.objects.filter(pub_date__time=datetime.time(14, 30))
# Entry.objects.filter(pub_date__time__range=(datetime.time(8), datetime.time(17)))
#
# # hour
# Event.objects.filter(timestamp__hour=23)
# SELECT ... WHERE EXTRACT('hour' FROM timestamp) = '23';
# Event.objects.filter(time__hour=5)
# SELECT ... WHERE EXTRACT('hour' FROM time) = '5';
# Event.objects.filter(timestamp__hour__gte=12)
# SELECT ... WHERE EXTRACT('hour' FROM timestamp) >= '12';
#
#  # minute
# Event.objects.filter(timestamp__minute=29)
# SELECT ... WHERE EXTRACT('minute' FROM timestamp) = '29';
# Event.objects.filter(time__minute=46)
# SELECT ... WHERE EXTRACT('minute' FROM time) = '46';
# Event.objects.filter(timestamp__minute__gte=29)
# SELECT ... WHERE EXTRACT('minute' FROM timestamp) >= '29';
#
# # second
# Event.objects.filter(timestamp__second=31)
# Event.objects.filter(time__second=2)
# Event.objects.filter(timestamp__second__gte=31)
# SELECT ... WHERE EXTRACT('second' FROM timestamp) = '31';
# SELECT ... WHERE EXTRACT('second' FROM time) = '2';
# SELECT ... WHERE EXTRACT('second' FROM timestamp) >= '31';
#
# # regex
# Entry.objects.get(title__regex=r'^(An?|The) +')
# SELECT ... WHERE title ~ '^(An?|The) +'; -- PostgreSQL
# SELECT ... WHERE title REGEXP '^(An?|The) +'; -- SQLite
#
# # iregex
# Entry.objects.get(title__iregex=r'^(an?|the) +')
# SELECT ... WHERE title ~* '^(an?|the) +'; -- PostgreSQL
# SELECT ... WHERE title REGEXP '(?i)^(an?|the) +'; -- SQLite

