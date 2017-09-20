from __future__ import unicode_literals
from django.shortcuts import HttpResponse, redirect, render


def index(request):
    context = {
        'greeting': 'A new app!?',
    }
    return render(request, 'book_authors/index.html', context)
