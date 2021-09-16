from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UpdateBook, UpdateCustomer, UpdateSeller
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def pagination(request, instanse):
    pagin = Paginator(instanse, 4)
    page = request.GET.get('page')
    page_obj = pagin.get_page(page)
    return page_obj


def book(request):
    if request.POST:
        curr_element = request.POST.get('id', None)
        elem = get_object_or_404(pk=curr_element, klass=Book)
        elem.delete()
        book = Book.objects.all()
    else:
        book = Book.objects.all()

    return render(request, 'book.html', {'content': pagination(request, book)})


def customer(request):
    if request.POST:
        id_customer = request.POST.get('id', None)
        curr_customer = get_object_or_404(pk=int(id_customer), klass=Customer)
        curr_customer.delete()
        customer = Customer.objects.all()
    else:
        customer = Customer.objects.all()
    return render(request, 'customer.html', {'content': pagination(request, customer)})


def update_book(request, book_id):
    if request.method == 'GET':
        upd_book = get_object_or_404(pk=int(book_id), klass=Book)
        form = UpdateBook(instance=upd_book)
    else:
        upd_book = get_object_or_404(pk=int(book_id), klass=Book)
        form = UpdateBook(request.POST, request.FILES, instance=upd_book)
        if form.is_valid():
            b = form.save(commit=False)
            b.save()
        return redirect('/book')
    return render(request, 'update_book.html', {'form': form, 'book_id': book_id})


def update_customer(request, customer_id):
    if request.method == 'GET':
        upd_customer = get_object_or_404(pk=int(customer_id), klass=Customer)
        form = UpdateCustomer(instance=upd_customer)
    else:
        upd_customer = get_object_or_404(pk=int(customer_id), klass=Customer)
        form = UpdateCustomer(request.POST, instance=upd_customer)
        if form.is_valid():
            cust = form.save(commit=False)
            cust.save()
        return redirect('/customer')
    return render(request, 'update_customer.html', {'form': form, 'customer_id': customer_id})


def seller(request):
    if request.POST:
        id_seller = request.POST.get('id', None)
        current_seller = get_object_or_404(pk=int(id_seller), klass=Seller)
        current_seller.delete()
        seller = Seller.objects.all()
    else:
        seller = Seller.objects.all()
    return render(request, 'seller.html', {'content': pagination(request, seller)})


def update_seller(request, seller_id):
    if request.method == "GET":
        upd_seller = get_object_or_404(pk=int(seller_id), klass=Seller)
        form = UpdateSeller(instance=upd_seller)
    else:
        upd_seller = get_object_or_404(pk=int(seller_id), klass=Seller)
        form = UpdateSeller(request.POST, request.FILES, instance=upd_seller)
        if form.is_valid():
            sel = form.save(commit=False)
            sel.save()
        return redirect('/seller')
    return render(request, 'update_seller.html', {'form': form, 'seller_id': seller_id})

def order(request):
    if request.POST:
        curr_ord = request.POST.get("id", None)
        ord_elem = get_object_or_404(pk=int(id_order))
    order = Order.objects.all()
    return render(request, 'order.htnl', {'content':pagination(request, order)})
