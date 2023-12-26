from django.templatetags.static import static
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static("base/icons/default-avatar.png")
