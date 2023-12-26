from django.contrib import admin

from .models import Problem, Category, Language


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = (
        "categories",
        "languages",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
