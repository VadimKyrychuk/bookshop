from django import forms
from .models import Book, Customer, Seller, Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UpdateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'name_product': 'Название книги',
            'price': "Цена",
            "genre": "Жанр",
            "img": "Изображение"
        }
        widgets = {
            'name_product': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            "genre": forms.Select(choices=Book.GENRE_LIST, attrs={'class': 'form-control'}),
            "img": forms.FileInput(attrs={'class': 'form-control'}),
        }


class UpdateCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'first_name': 'Имя ',
            'last_name': 'Фамилия',
            'phone': 'Номер телефона',
            'email': 'Email',
            'discount': 'Скидочная карта'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'discount': forms.CheckboxInput()
        }


class UpdateSeller(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Номер телефона',
            'email': 'Email',
            'position': 'Должность',
            'img': 'Изображение',
            'recruitment': 'Дата принятия на работу'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.Select(choices=Seller.POSITION_LIST, attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'recruitment': forms.SelectDateWidget(),
        }


class UpdateOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Покупатель',
            'seller': 'Продавец',
            'product': 'Книга',
            'date': 'Дата покупки',
            'total': 'Сумма',
        }

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'seller': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-select'}),
            'total': forms.TextInput(attrs={'class': 'form-control',
                                            'type': 'number'}),
        }


class Report1(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['seller']

    labels = {'seller': 'Продавец'}
    widget = {'seller': forms.Select(attrs={'class': 'form-select'})}


class OrderDate(forms.Form):
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                        'type': 'date'}), label="Дата продажи")


class SellerProduct(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']

    labels = {'product': 'Товар'}
    widget = {'product': forms.Select(attrs={'class': 'form-select'})}

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

