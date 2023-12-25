from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        validators=[
            MinLengthValidator(11, "Phone Number must contain 11 characters")
        ],
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static("static/icons/default-avatar.png")

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
