from django.contrib import admin

from .models import Contest


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "start_time",
        "is_contest_active",
        "is_registration_open",
    )
    list_filter = ("is_active",)
