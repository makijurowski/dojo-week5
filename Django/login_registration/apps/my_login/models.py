# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import re


# Regex for validation
NAME_REGEX = re.compile(r"^[a-zA-Z\\s]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASS_UPPER = re.compile(r"[A-Z{1,5}]")
PASS_DIGIT = re.compile(r"\d{1,5}")


class UserManager(models.Manager):
    def validate_registration(self, registration_data):
        errors = []
        existing_user = User.objects.filter(email=registration_data['email'])

        # Make sure all fields have been filled
        if (len(registration_data['first_name']) <= 0 or len(registration_data['last_name']) or len(registration_data['email']) <= 0 or len(registration_data['password']) <= 0 or len(registration_data['password_confirm'] <= 0)):
                errors.append('Please enter every field to continue.')

        # Check length and characters of name
        if (len(registration_data['first_name']) < 2 or len(registration_data['last_name']) < 2):
                errors.append('Your name must contain 3 or more characters.')
        elif not re.match(NAME_REGEX, registration_data['first_name']) or not re.match(NAME_REGEX, registration_data['last_name']):
            errors.append('Please use only alphanumeric letters for your first and last name.')

        # Check email formatting and uniqueness
        if not re.match(EMAIL_REGEX, registration_data['email']):
            errors.append('Please enter a valid email address.')
        elif not len(existing_user) > 0:
            errors.append('This email is already registered to an account.')

        # Check if password is valid amd matches confirmation
        if not re.match(PASS_DIGIT, registration_data['password']) or re.match(PASS_UPPER, registration_data['password']):
            errors.append('Your password must contain at least one number and uppercase letter.')
        elif registration_data['password'] != registration_data['password_confirm']:
            errors.append('Your passwords do not match. Please try again.')

        # Return any errors
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
