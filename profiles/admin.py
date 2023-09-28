"""
Profiles app admin module.

    Models registration
"""

from django.contrib import admin

from .models import Profile


admin.site.register(Profile)
