from django.contrib import admin

from .models import Category, Product, ProductImage
# Register your models here.


class ProductsImagesInline(admin.TabularInline):
    model = ProductImage
    fields = ['image', ]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImagesInline, ]
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
