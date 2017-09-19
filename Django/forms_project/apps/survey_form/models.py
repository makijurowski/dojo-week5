# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Form(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
