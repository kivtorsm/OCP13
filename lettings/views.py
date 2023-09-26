from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    View showing list of lettings
    :param request: http request activated by user
    :return: render of the request with the appropriate template and the list of lettings
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Shows details of a letting
    :param request: http request activated by user
    :param letting_id: letting identification for a letting
    :return: render of the request with the letting detail template and the context (title, address)
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
