# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponse, redirect, render
from .forms import UserForm, ProfileForm, SimpleTable
from .models import User, Profile

# GET request to /users, displays all (template)
# /users
def index(request):
    return HttpResponse('Hello there!~')

# GET request to add a new user, displays form (template)
# /users/new
def new(request):
    pass

# GET request to edit a user, displays form to edit (template)
# /users/<id>/edit
@login_required
@transaction.atomic
def edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:edit')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'restful_users/edit_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# GET request to display info on a user (template)
def show(request):
    pass

# POST request to insert a new user in db
# Used on /users/new and redirect to /users/<id>
def create(request):
    pass

# GET request removes a user with given id
# Redirect back to /users
def destroy(request):
    pass

# POST request to process submitted update form
# Used on /users/<id>/edit and redirect to /users/<id>
def update(request):
    pass

# Simple table
def users_list(request):
    queryset = User.objects.all()
    table = SimpleTable(queryset)
    return render(request, 'restful_users/show_all.html', {'table': table})
