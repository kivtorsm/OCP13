from django.urls import reverse, resolve


def test_homepage_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()


def test_homepage_url(client):
    path = reverse('index')
    assert path == '/'
    assert resolve(path).view_name == 'index'


def test_should_return_admin_page(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200
