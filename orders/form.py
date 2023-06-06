
from . models import Customer
from django import forms
class CustomerForm(forms.Form):
    adress = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-input-size','placeholder':'Manzilni kiriting'}
        ),
        label='Manzil'
    )
