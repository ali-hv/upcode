from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "username",
        "email",
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
