from django.contrib import admin

from .models import Problem, Tag, Language, Submission


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "contest", )
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


@admin.register(Submission)
class UserProblemAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "problem",
        "score",
        "status",
    )
