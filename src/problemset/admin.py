from django.contrib import admin

from .models import Problem, Tag, Language


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = (
        "categories",
        "languages",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
