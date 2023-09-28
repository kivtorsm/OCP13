"""
oc_lettings_site app views :
    - Index :
        Homepage
"""
from django.shortcuts import render


def index(request):
    """
    View showing the homepage
    :param request: http request activated by user
    :return: render of the request with the indicated template.
    """
    return render(request, 'index.html')
