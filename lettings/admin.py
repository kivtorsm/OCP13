from django.contrib import admin
from .models import Address, Letting

# Register of app models for the admin interface

admin.site.register(Address)
admin.site.register(Letting)
