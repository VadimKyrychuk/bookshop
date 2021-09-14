from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def book(request):
    book = Book.objects.all()
    pagination = Paginator(book, 4)
    page = request.GET.get('page')
    page_obj = pagination.get_page(page)

    return render(request, 'book.html', {'book': page_obj})
