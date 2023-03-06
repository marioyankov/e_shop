from django.contrib import admin
from .models import Category, Product


class CategoryViewAdmin(admin.ModelAdmin):
    list_display = ('name')
    prepopulated_fields = {"slug": ("name",)}

class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryViewAdmin)
admin.site.register(Product, ProductViewAdmin)