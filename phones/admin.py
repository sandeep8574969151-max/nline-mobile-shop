from django.contrib import admin
from .models import Product, Brand  # <--- Yeh line sabse zaroori hai

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Admin panel mein kaunse columns dikhenge
    list_display = ('name', 'category', 'brand', 'price', 'store_name')
    
    # Side mein filter ka option (Mobiles, Laptops, etc. ke liye)
    list_filter = ('category', 'brand', 'store_name')
    
    # Search bar ke liye
    search_fields = ('name', 'brand__name')
    
    # Name likhte hi Slug apne aap ban jayega
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


