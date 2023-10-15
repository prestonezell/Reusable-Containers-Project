from django.contrib import admin
from .models import Product

admin.site.register(Product)
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'product_name', 'material_type', 'price', 'is_available', 'with_collector', 'product_id')