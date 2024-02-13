from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True)
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None

    phone_number = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11, "Phone Number must contain 11 characters")],
    )

    def __str__(self):
        return self.username
