from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    phone_number = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11, "Phone Number must contain 11 characters")],
    )

    def __str__(self):
        return self.username
