from django.shortcuts import render

from profiles.models import Profile


def index(request):
    """
    View showing list of profiles
    :param request: http request activated by user
    :return: render of the request with the appropriate template and the list of profiles
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Shows details of a profile
    :param request: http request activated by user
    :param username: username string needed to look for a profile and show details
    :return: render of the request with the profile detail template and the context (profile)
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
