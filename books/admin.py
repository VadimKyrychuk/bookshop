from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Seller, Order, Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'discount']
    list_filter = ['discount']


@admin.register(Seller)
class AdminSeller(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'recruitment', 'pic']

    def pic(self, obj):
        return mark_safe('<img src="{url}" width="150" height="200" />'.format(url=obj.img.url))


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['name_product', 'price', 'genre', 'pic']
    list_filter = ['genre']

    def pic(self, obj):
        return mark_safe('<img src="{url}" width="150" height="200" />'.format(url=obj.img.url))


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass
