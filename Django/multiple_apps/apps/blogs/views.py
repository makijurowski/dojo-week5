# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    context = {
        'email': 'makiroggers@gmail.com',
        'name': 'Maki',
    }
    response = "INDEX IT placeholder to later display all the list of blogs"
    return render(request, 'blogs/index.html', context)


def new(request):
    response = "NEW IT placeholder to display a new form to create a new blog"
    return HttpResponse(response)


def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")


def show(request, num):
    response = "SHOW IT placeholder to later display all the list of blogs"
    return HttpResponse(response)


def edit(request, num):
    response = "EDIT ITplaceholder to later display all the list of blogs"
    return HttpResponse(response)


def destroy(request, num):
    response = "DESTROY IT to later display all the list of blogs"
    return HttpResponse(response)
