from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User


class Registration_Form(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.CharField(label = 'Email address', widget = forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class': 'form-control'}))
    password_confirm=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password',
                  'password_confirm')
