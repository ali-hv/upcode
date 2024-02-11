from django.contrib import admin

from .models import Problem, Tag, Language, Submission, TestCase


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "level",
        "contest",
    )
    search_fields = (
        "categories",
        "languages",
    )


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ("problem",)


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
        "language",
        "score",
        "status",
        "submitted_date",
    )
