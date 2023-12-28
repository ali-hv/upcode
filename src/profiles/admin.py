from django.contrib import admin
from .models import Profile, UserProblem


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "get_full_name",
    )


@admin.register(UserProblem)
class UserProblemAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "problem",
        "status",
    )
