from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile class including the user and the favorite city
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Shows a string when printing the class instance
        :return: username string
        """
        return self.user.username
