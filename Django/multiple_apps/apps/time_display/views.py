# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    response = {
        'date': strftime("%A, %B %d, %Y", localtime()),
        'time': strftime("%I:%M:%S %p %Z", localtime())
    }
    return render(request, 'time_display/index.html', response)
