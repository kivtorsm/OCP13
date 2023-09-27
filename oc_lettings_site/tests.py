
def test_should_return_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()


def test_should_return_admin_page(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200
