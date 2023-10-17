# """
# Test module with all oc_lettings_site app tests:
#     - test_profiles_list_url
#     - test_profiles_list_view
#     - test_profile_model
#     - test_profile_detail_url
#     - test_profiles_detail_view
# """
#
#
# import pytest
#
# from django.urls import reverse, resolve
# from django.contrib.auth.models import User
#
# from pytest_django.asserts import assertTemplateUsed
#
# from profiles.models import Profile
#
#
# def test_profiles_list_url():
#     """
#     Tests url for showing the profiles list :
#         - Correct path for the url name
#         - Correct view name for the url name path
#     :return: none
#     """
#     path = reverse('profiles:index')
#     assert path == '/profiles/'
#     assert resolve(path).view_name == 'profiles:index'
#
#
# @pytest.mark.django_db
# def test_profiles_list_view(client):
#     """
#     Tests view for showing the lettings list :
#         - Status code 200
#         - 'Profiles' included in the response content
#     :param client: client used for mocking http requests
#     :return: none
#     """
#     response = client.get('/profiles/')
#     assert response.status_code == 200
#     assert "Profiles" in response.content.decode()
#
#
# @pytest.mark.django_db
# def test_profile_model():
#     """
#     Tests profile model :
#         - Correct printing of profile model
#     :return: none
#     """
#     user = User.objects.create_user('mock-user')
#     profile = Profile.objects.create(
#         user=user,
#         favorite_city="Paris",
#     )
#
#     expected_value = "mock-user"
#     assert str(profile) == expected_value
#
#
# @pytest.mark.django_db
# def test_profile_detail_url():
#     """
#     Tests url for showing a profile details :
#         - Created profile path corresponds to expected value
#         - View name used in the path corresponds to expected view
#     :return: none
#     """
#     user = User.objects.create_user('mock-user')
#     Profile.objects.create(
#         user=user,
#         favorite_city="Paris",
#     )
#     path = reverse('profiles:profile', kwargs={'username': 'mock-user'})
#
#     assert path == '/profiles/mock-user/'
#     assert resolve(path).view_name == 'profiles:profile'
#
#
# @pytest.mark.django_db
# def test_profiles_detail_view(client):
#     """
#     Tests view for a profile detail :
#         - Status code 200
#         - Expected content inside request
#         - Template used in render corresponds to expected template
#     :param client: client used for mocking http requests
#     :return: none
#     """
#     user = User.objects.create_user('mock-user')
#     Profile.objects.create(
#         user=user,
#         favorite_city="Paris",
#     )
#
#     path = reverse('profiles:profile', kwargs={'username': "mock-user"})
#
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = "mock-user"
#
#     assert response.status_code == 200
#     assert expected_content in content
#     assertTemplateUsed(response, "profiles/profile.html")
