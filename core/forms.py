from django import forms
from .models import Product, Client
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['arabic_name', 'name', 'price', 'wholesale_price', 'distribution_price', 'cost_price', 'quantity']
      
class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ("arabic_name","name","phone1", "balance", "camion", "address", "serial", "nif", "nis")

