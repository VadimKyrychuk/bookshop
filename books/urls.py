from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('book', book, name='book'),
    path('book/<int:book_id>', update_book, name='update_book'),
]

