from django.contrib import admin
from .models import Product, Stock, StockProduct
# Register your models here.

class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]
    inlines = [StockProductInline,]


@admin.register(Stock)
class StocktAdmin(admin.ModelAdmin):
    list_display = ['address',]
    inlines = [StockProductInline,]