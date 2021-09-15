from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def book(request):
    if request.POST:
        curr_element = request.POST.get('id', None)
        elem = get_object_or_404(pk=curr_element, klass=Book)
        elem.delete()
        book = Book.objects.all()
    else:
        book = Book.objects.all()
    pagination = Paginator(book, 4)
    page = request.GET.get('page')
    page_obj = pagination.get_page(page)
    return render(request, 'book.html', {'book': page_obj})


def update_book(request, book_id):
    if request.GET:
        