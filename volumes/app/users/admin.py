from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from profiles.models import Profile
from .models import User


class UserProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [UserProfileInline]
    list_display = (
        "email",
        "username",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_superuser",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "phone_number", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                    "date_joined",
                    "last_login",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "username",
    )
    ordering = (
        "is_superuser",
        "is_staff",
        "date_joined",
    )
