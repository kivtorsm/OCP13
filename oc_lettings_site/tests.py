from django.urls import reverse, resolve

from pytest_django.asserts import assertTemplateUsed


def test_homepage_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
    assertTemplateUsed(response, 'index.html')


def test_homepage_url():
    path = reverse('index')
    assert path == '/'
    assert resolve(path).view_name == 'index'


def test_should_return_admin_page(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


def test_404(client):
    response = client.get("/asdf/")
    assert response.status_code == 404
    assert "oops-erreur-404-illustration-concept-robot-casse_114360-5529.avif" in response.content.decode()
