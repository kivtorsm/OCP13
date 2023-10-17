# """
# Test module with all oc_lettings_site app tests:
#     - test_homepage_view
#     - test_homepage_url
#     - test_should_return_admin_page
#     - test_404
# """
#
#
# from django.urls import reverse, resolve
#
# from pytest_django.asserts import assertTemplateUsed
#
#
# def test_homepage_view(client):
#     """
#     Tests homepage view :
#         - Status code 200
#         - Title in response content
#         - Template used corresponds to expected
#     :param client: client used for mocking http requests
#     :return: none
#     """
#     response = client.get('/')
#     assert response.status_code == 200
#     assert "Welcome to Holiday Homes" in response.content.decode()
#     assertTemplateUsed(response, 'index.html')
#
#
# def test_homepage_url():
#     """
#     Tests homepage url :
#         - Path corresponds to expected
#         - Used view name corresponds to expected
#     :return: none
#     """
#     path = reverse('index')
#     assert path == '/'
#     assert resolve(path).view_name == 'index'
#
#
# def test_should_return_admin_page(admin_client):
#     """
#     Tests admin page view :
#         - Status code 200
#     :param admin_client: client used for mocking http requests
#     :return: none
#     """
#     response = admin_client.get('/admin/')
#     assert response.status_code == 200
#
#
# def test_404(client):
#     """
#     Tests homepage view :
#         - Status code 404
#         - Personalized image present in response content
#     :param client: client used for mocking http requests
#     :return: none
#     """
#     response = client.get("/asdf/")
#     assert response.status_code == 404
#     assert "oops-erreur-404-illustration-concept-robot-casse_114360-5529.avif" in response.content.decode()
