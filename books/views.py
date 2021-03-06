from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import *
from .forms import UpdateBook, UpdateCustomer, UpdateSeller, UpdateOrder, Report1, OrderDate, SellerProduct, UserRegisterForm, UserLoginForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout, login as user_login


def pagination(request, instanse):
    pagin = Paginator(instanse, 4)
    page = request.GET.get('page')
    page_obj = pagin.get_page(page)
    return page_obj


def home(request):
    return render(request, 'home.html')


def book(request):
    search_query = request.GET.get('search_query', None) or request.POST.get('search_query', '')
    if request.POST:
        curr_element = request.POST.get('id', None)
        elem = get_object_or_404(pk=curr_element, klass=Book)
        elem.delete()
        book = Book.objects.all() if not search_query else Book.objects.filter \
            (Q(name_product__icontains=search_query))
    else:
        book = Book.objects.all() if not search_query else Book.objects.filter \
            (Q(name_product__icontains=search_query))
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
        ord_elem = get_object_or_404(pk=int(curr_ord), klass=Order)
        ord_elem.delete()
        order = Order.objects.all()
    else:
        order = Order.objects.all()
    return render(request, 'order.html', {'content': pagination(request, order)})


def update_order(request, order_id):
    if request.method == "GET":
        current_order = get_object_or_404(pk=int(order_id), klass=Order)
        form = UpdateOrder(instance=current_order)
    else:
        current_order = get_object_or_404(pk=int(order_id), klass=Order)
        form = UpdateOrder(request.POST, instance=current_order)
        if form.is_valid():
            element = form.save(commit=False)
            element.save()
        return redirect('/order')
    return render(request, 'update_order.html', {'form': form, 'order_id': order_id})


def seller_buyers(request):
    form = Report1()
    seller_buyers = Order.objects.filter(seller__pk=request.POST.get('seller'))
    id_custom = []
    custom = []
    for i in seller_buyers:
        if not i.customer.id in id_custom:
            custom.append(i.customer)
            id_custom.append(i.customer.id)
    if custom:
        form = Report1(request.POST)
    return render(request, 'seller_buyers.html', {'form': form, 'content': custom})


def order_date(request):
    form = OrderDate
    content = Order.objects.filter(date=request.POST.get('date'))
    if request.POST:
        form = OrderDate(request.POST)
    return render(request, 'orderdate.html', {'form': form, 'content': content})


def seller_product(request):
    form = SellerProduct
    filtered = Order.objects.filter(product__pk=request.POST.get('product'))
    id_seller = []
    content = []
    for i in filtered:
        if not i.seller.id in id_seller:
            id_seller.append(i.seller.id)
            content.append(i)
    if request.POST:
        form = SellerProduct(request.POST)
    return render(request, 'sellerproduct.html', {'form': form, 'content': content})


def customer_product(request):
    form = SellerProduct
    filtered = Order.objects.filter(product__pk=request.POST.get('product'))
    id_customer = []
    content = []
    for i in filtered:
        if not i.seller.id in id_customer:
            id_customer.append(i.customer.id)
            content.append(i)
    if request.POST:
        form = SellerProduct(request.POST)
    return render(request, 'customer_product.html', {'form': form, 'content':content})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/login')
        else:
            pass
    else:
        form = UserRegisterForm()
    return render(request, 'authorization/register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

