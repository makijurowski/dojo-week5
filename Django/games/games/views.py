# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):
    return redirect('/ninja_gold')

