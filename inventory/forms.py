from .models import Drug,  Order
from django import forms

class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name','price','quantity']
    



class AddOrderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'address','phone','drug','quantity']
       
