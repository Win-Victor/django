from django.contrib import admin

from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category',)
    fields = ('name', 'category', 'image', 'description', ('price', 'quantity'))
    readonly_fields = ('category',)
    ordering = ('name',)
    search_fields = ('name',)
