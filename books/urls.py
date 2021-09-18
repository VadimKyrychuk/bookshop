from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('book', book, name='book'),
    path('customer', customer, name='customer'),
    path('seller', seller, name='seller'),
    path('order', order, name='order'),
    path('seller_buyers', seller_buyers, name='seller_buyers'),
    path('book/<int:book_id>', update_book, name='update_book'),
    path('customer/<int:customer_id>', update_customer, name='update_customer'),
    path('seller/<int:seller_id>', update_seller, name='update_seller'),
    path('order/<int:order_id>', update_order, name='update_order'),
]

