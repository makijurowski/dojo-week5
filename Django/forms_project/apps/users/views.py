# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User


def index(request):
    context = {
        'all_users': User.objects.all(),
        'last_user': User.objects.order_by('-created_at').reverse()[:1],
        'first_user': User.objects.first(),
        'all_users_first_name_desc': User.objects.order_by('first_name'),
        'get_record_3': User.objects.get(id=3),
        'update_record_3': "get_record_3.last_name='Kinne'.save()",
        'save_record_3': get_record_3.save(),
        'delete_record_4': User.objects.get(id=4).delete(),
    }
    return render(request, 'users/index.html', context)

"""
VALIDATION IN SHELL COMMANDS:
for user in User.objects.all():
    ...:     if len(user.first_name) < 5:
    ...:         print user.first_name
    ...:     else:
    ...:         print "All good"

"""
