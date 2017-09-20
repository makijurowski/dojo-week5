# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.


def index(request):
    return redirect('/ninja_gold')

