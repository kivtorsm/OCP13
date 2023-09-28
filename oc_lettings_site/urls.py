"""
Urls module for main oc_lettings_site app:
    - Homepage
    - admin
"""


from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
