# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random
import string


def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Create your views here.
def index(request):
    if 'attempt_count' not in request.session:
        request.session['attempt_count'] = 0
    return render(request, 'words/index.html')

def reset(request):
    if request.method == "GET":
        del request.session['attempt_count']
        return redirect('index')

def generate(request):
    if request.method =="GET":
        request.session['attempt_count'] += 1
        request.session['new_word'] = random_generator()
    return redirect('index')
    
