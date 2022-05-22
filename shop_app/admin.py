from django.contrib import admin
from .models import Category, Product, Order
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('varcode','name','price','amount')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','create_date', 'complete_date')