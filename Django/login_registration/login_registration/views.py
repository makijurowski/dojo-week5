from django.contrib.auth import logout
from django.shortcuts import HttpResponse, redirect, render

def index(request):
    response = 'Placeholder to verify project rendering.'
    return render(request, 'base.html', response)


def logout_view(request):
    logout(request)

def base(request):
    response = 'Placeholder to check project rendering.'