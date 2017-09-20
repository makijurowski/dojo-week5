# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponseRedirect


# Create your views here.
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    return render(request, 'ninja_gold/index.html')


def process_money(request):
    pass
    # Checks input to assign values