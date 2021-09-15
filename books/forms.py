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
            'price': forms.DecimalField(),
            "genre": forms.ChoiceField(),
            "img": forms.ImageField(attrs={'class':'form-control'}),

        }
