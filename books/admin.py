from django.contrib import admin
from .models import Book, Seller, Order, Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    pass


@admin.register(Seller)
class AdminSeller(admin.ModelAdmin):
    pass


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass
