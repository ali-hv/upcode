from django.templatetags.static import static
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static("home/images/icons/default-avatar.png")
