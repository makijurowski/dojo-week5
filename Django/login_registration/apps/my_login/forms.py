from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User


class UserForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        # widgets = {
        #     'password': forms.Password(Input(),)
        # }
        fields = ('first_name', 
                  'last_name', 
                  'email', 
                  'password', )
