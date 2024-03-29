from django.contrib import admin
from .models import Product, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "price", "description"]})
    ]
    inlines = [ImageInline]
    
admin.site.register(Product, ProductAdmin)
