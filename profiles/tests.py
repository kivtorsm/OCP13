import pytest

from django.urls import reverse, resolve
from django.contrib.auth.models import User

from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


def test_profiles_list_url():
    path = reverse('profiles:index')
    assert path == '/profiles/'
    assert resolve(path).view_name == 'profiles:index'


@pytest.mark.django_db
def test_profiles_list_view(client):
    response = client.get('/profiles/')
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_profile_model():
    user = User.objects.create_user('mock-user')
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris",
    )

    expected_value = "mock-user"
    assert str(profile) == expected_value


@pytest.mark.django_db
def test_profile_detail_url():
    user = User.objects.create_user('mock-user')
    Profile.objects.create(
        user=user,
        favorite_city="Paris",
    )
    path = reverse('profiles:profile', kwargs={'username': 'mock-user'})

    assert path == '/profiles/mock-user/'
    assert resolve(path).view_name == 'profiles:profile'


@pytest.mark.django_db
def test_profiles_detail_view(client):
    user = User.objects.create_user('mock-user')
    Profile.objects.create(
        user=user,
        favorite_city="Paris",
    )

    path = reverse('profiles:profile', kwargs={'username': "mock-user"})

    response = client.get(path)
    content = response.content.decode()
    expected_content = "mock-user"

    assert response.status_code == 200
    assert expected_content in content
    assertTemplateUsed(response, "profiles/profile.html")
