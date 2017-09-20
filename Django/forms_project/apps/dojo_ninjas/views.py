# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime


def index(request):
    context = {
        'greeting': 'Hello there!',
    }
    return render(request, 'dojo_ninjas/index.html', context)
