from django import forms
from .models import Book


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
            'name_product': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'type':'number', 'class':'form-control'}),
            "genre": forms.Select(choices=Book.GENRE_LIST, attrs={'class': 'form-control'}),
            "img": forms.FileInput(attrs={'class':'form-control'}),

        }
