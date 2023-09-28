"""
Test module with all lettings app tests:
    - test_lettings_list_url
    - test_lettings_list_view
    - test_lettings_model
    - test_address_model
    - test_letting_detail_url
    - test_lettings_detail_view
    - test_404
"""

import pytest

from django.urls import reverse, resolve

from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address


def test_lettings_list_url():
    """
    Tests url for showing the lettings list :
        - Correct path for the url name
        - Correct view name for the url name path
    :return: none
    """
    path = reverse('lettings:index')
    assert path == '/lettings/'
    assert resolve(path).view_name == 'lettings:index'


@pytest.mark.django_db
def test_lettings_list_view(client):
    """
    Tests view for showing the lettings list :
        - Status code 200
        - 'Lettings' included in the response content
    :param client: client used for mocking http requests
    :return: none
    """
    response = client.get('/lettings/')
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_lettings_model():
    """
    Tests letting model :
        - Correct printing of lettings model
    :return: none
    """
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
    """
    Tests address model :
        - Expected address printing format
    :return: none
    """
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
    """
    Tests url for showing a lettings details :
        - Created lettings path corresponds to expected value
        - View name used in the path corresponds to expected view
    :return: none
    """
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
    """
    Tests view for a letting detail :
        - Status code 200
        - Expected content inside request
        - Template used in render corresponds to expected template
    :param client: client used for mocking http requests
    :return: none
    """
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


@pytest.mark.django_db
def test_404(client):
    """
    Tests error 500 personalized page
        - Status code 500
        - Personalized image found in request content
    :return: none
    """
    response = client.get("/lettings/1/")
    assert response.status_code == 404
    assert "oops-erreur-404-illustration-concept-robot-casse_114360-5529.avif" in response.content.decode()
