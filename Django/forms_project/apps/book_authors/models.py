# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    author_id = models.ManyToManyField('Author', through='BookAuthor', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    book_id = models.ManyToManyField('Book', through='BookAuthor', blank=True)
    notes = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)


"""
QUERIES:
Retrieve all authors for the 3rd book

Retrieve all authors for Book 3
b3_a = BookAuthor.objects.filter(book=3).author

Retrieve Author Names:
for each in b3_a:
    try:
        print Author.objects.get(id=each.author.id).first_name
    except:
        print "Nothing here."
"""
