from django.contrib import admin

from apps.products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    search_fields = ('title', 'description', 'price')