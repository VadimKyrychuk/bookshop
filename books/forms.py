from django import forms
from .models import Book, Customer, Seller


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
