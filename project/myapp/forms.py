from django.forms import ModelForm
from .models import Products
from django import forms

# Code added for loading form data on the Booking page
class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"