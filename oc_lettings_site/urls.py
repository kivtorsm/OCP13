"""
Urls module for main oc_lettings_site app:
    - Homepage
    - admin
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    # path('sentry-debug/', trigger_error),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)