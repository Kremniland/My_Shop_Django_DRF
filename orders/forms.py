from django import forms

from orders.models import Oreders


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Иван'}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Иван'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'you@example.com'}
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Россия, Москва, ул. Мира, дом 6',
    }))

    class Meta:
        model = Oreders
        fields = ('first_name', 'last_name', 'email', 'address')

