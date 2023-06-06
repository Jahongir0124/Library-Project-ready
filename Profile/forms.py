from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
class UserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'int'}
        ),
        max_length=100
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        max_length=100
    )


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',"password1"]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder':'Foydalauvchi nomi'}
        ),
        label = 'Foydalanuvchi nomi',
        max_length=100
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Ismingiz'}
        ),
        label='ISM',
        max_length=100
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder':'Familiyangizni kiritng'}
        ),
        label = 'Familiya',
        max_length=100
    )

    email = forms.EmailInput(
        attrs={
            'class':'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Email'
        }
    )
    
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control','placeholder':'Parol'}
        ),
        label='Parol',
        max_length=100
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Parol2'}
        ),
        label='Parolni tasdiqlash',
        max_length=100
    )



