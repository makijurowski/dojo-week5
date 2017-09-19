# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from .models import Form
from .forms import PostSurvey


# Create your views here.
def index(request):
    response = {
        'text': 'This is my survey_form apps response.'
    }
    return render(request, 'survey_form/index.html', response)

def process(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0
    print "This worked!"
    request.session['fname'] = request.POST.get('fname')
    request.session['lname'] = request.POST.get('lname')
    request.session['dojo_location'] = request.POST.get('dojo_location')
    request.session['language_options'] = request.POST.get('language_options')
    request.session['opt_comment'] = request.POST.get('opt_comment')
    request.session['attempts'] += 1
    return redirect('results')


def results(request):
    response = {
        'text': 'Your registration was successful!',
        'fname': request.session['fname'],
        'lname': request.session['lname'],
        'dojo_location': request.session['dojo_location'],
        'language_options': request.session['language_options'],
        'opt_comment': request.session['opt_comment'],
        'attempts': request.session['attempts']
    }
    return render(request, 'survey_form/success.html', response)
