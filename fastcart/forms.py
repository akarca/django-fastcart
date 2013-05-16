from django import forms
from django.contrib.contenttypes.models import ContentType

from .models import CartItem
from . import get_product_model


class CartItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=get_product_model().objects.all())
    quantity = forms.IntegerField(min_value=1,
                                  initial=1,
                                  required=False)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        return quantity if quantity is not None else 1

    def add_to_cart(self, cart):
        return cart.add(self.cleaned_data['product'],
                        self.cleaned_data['quantity'])


class UpdateCartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1,
                                  initial=1,
                                  required=False)

    class Meta:
        model = CartItem
        fields = ('quantity',)

    def __init__(self, *args, **kwargs):
        super(UpdateCartItemForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].required = False

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        return quantity if quantity is not None else 1
