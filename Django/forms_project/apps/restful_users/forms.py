from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import django_tables2 as tables


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Optional')
    email = forms.EmailField(max_length=255,
                             help_text='Required')
    class Meta:
        model = User
        fields = ('username',
                  'first_name', 
                  'last_name', 
                  'email',
                  'password1',
                  'password2')


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')


class SimpleTable(tables.Table):
    
    class Meta:
        model = User
