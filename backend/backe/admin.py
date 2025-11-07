from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'store', 'category', 'price', 'created_at']
    list_filter = ['store', 'category', 'created_at']
    search_fields = ['title', 'category']
    ordering = ['-created_at']


