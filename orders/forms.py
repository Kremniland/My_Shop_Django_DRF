from django import forms

from orders.models import Oreders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Oreders
        fields = ('first_name', 'last_name', 'email', 'address')

