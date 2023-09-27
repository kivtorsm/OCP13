import pytest

from django.urls import reverse, resolve

from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address


def test_lettings_list_url():
    path = reverse('lettings:index')
    assert path == '/lettings/'
    assert resolve(path).view_name == 'lettings:index'


@pytest.mark.django_db
def test_lettings_list_view(client):
    response = client.get('/lettings/')
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_lettings_model():
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(
        title="Joshua Tree Green Haus /w Hot Tub",
        address=address
    )
    expected_value = "Joshua Tree Green Haus /w Hot Tub"
    assert str(letting) == expected_value


@pytest.mark.django_db
def test_address_model():
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )

    expected_value = "7217 Bedford Street"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_detail_url():
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    Letting.objects.create(
        title="Joshua Tree Green Haus /w Hot Tub",
        address=address,
    )
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    assert path == '/lettings/1/'
    assert resolve(path).view_name == 'lettings:letting'


@pytest.mark.django_db
def test_lettings_detail_view(client):
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    Letting.objects.create(
        title="Joshua Tree Green Haus /w Hot Tub",
        address=address,
    )
    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    response = client.get(path)
    content = response.content.decode()
    expected_content = "Joshua Tree Green Haus /w Hot Tub"

    assert response.status_code == 200
    assert expected_content in content
    assertTemplateUsed(response, "lettings/letting.html")
