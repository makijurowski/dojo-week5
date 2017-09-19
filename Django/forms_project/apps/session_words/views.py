# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import strftime


# Create your views here.
def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    return render(request, 'session_words/index.html')

def add(request):
    request.session['new_word'] = request.POST.get('word')
    print request.session['new_word']
    request.session['color'] = request.POST.get('color')
    request.session['size'] = request.POST.get('big')
    request.session['created_at'] = strftime("%b %d, %Y: %H:%M %p")
    new_word_details = {
        'new_word': request.session['new_word'],
        'color': request.session['color'],
        'size': request.session['size'],
        'timestamp': request.session['created_at'],
    }
    request.session['word_list'].append(new_word_details)
    return redirect(index)
    # return render(request, 'session_words/index.html', new_word_details)
    
def reset(request):
    del request.session['word_list']
    return redirect(index)
