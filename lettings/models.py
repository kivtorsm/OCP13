"""
Models module :
    - Address
    - Letting
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Adress model.
    ...
    Attributes
    ----------
    number: int
        Street number
    street: str
        Street name
    city: str
        City name
    state: str
        State name
    zip_code: int
        postal zip code
    country_iso_code: str
        country international iso code

    Methods
    -------
    __str__:
        prints a string when the instance is printed
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns the number and the name of the street from the address
        :return: number and name of street of the address instance
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Allows to supercharge the plural of address
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Letting model. Represents a propery that can be let.
    ...
    Attributes
    ----------
    title: str
        Title for the letting
    address: Address
        Address where the letting is located

    Methods
    -------
    __str__:
        prints a string when the instance is printed
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Shows a printed name of the model with the title
        :return: string with the title of the model instance
        """
        return self.title
