from django import forms
from books.models import Profile

class ProfileForm(forms.ModelForm):
    city = forms.CharField(label='Город', max_length=64, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(label="Телефон",max_length=64, widget=forms.TextInput(attrs={'class':'form-control', 'type':'tel'}))
    avatar = forms.FileField(label="Телефон",max_length=64, widget=forms.FileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=64, label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}) )
    last_name = forms.CharField(max_length=64, label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}) )
    class Meta:
        model = Profile
        fields = ( 'last_name', 'first_name', 'city', 'phone', 'avatar')