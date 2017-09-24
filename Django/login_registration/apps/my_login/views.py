# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render, reverse
import bcrypt

from .forms import *
from .models import *


def index(request):
    context = {
        'new_user_registration': Registration_Form,
    }
    return render(request, 'my_login/index.html', context)


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass


def success(request):
    pass
