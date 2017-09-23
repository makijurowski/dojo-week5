# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect, render
from .models import *
from .forms import *
import os

def index(request):
    print "This worked 1!"
    # form = UserForm()
    context = {
        'base_template': "os.path.join(settings.FILES_DIR, '../base.html')",
    }
    print context
    return render(request, 'my_login/home.html', context=context)

def register(request):
    print "This worked 2!"
    if request.method == 'POST':
        print "This worked 3!"
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            userObj = form.cleaned_data
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            # username = usrObj['username']
            email = userObj['email']
            password = userObj['password']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            if not (User.objects.filter(email=email).exists()):
                user = User.create_user('first_name', 'last_name', 'email', 'password')
                user = authenticate(first_name = first_name, email = email, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('A user with that email already exists.')
        return render(request, 'my_login/index.html')
        # return HttpResponseRedirect('my_login/index.html')
    else:
        print "This worked 4!"
        form = UserForm()
    return render(request, 'my_login/index.html', {'form': form})
