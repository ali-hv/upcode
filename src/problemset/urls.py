from django.urls import path

from .views import Problemset, ProblemPage

app_name = "problemset"

urlpatterns = [
    path("", Problemset.as_view(), name="problemset"),
    path("<pk>", ProblemPage.as_view(), name="problem_page")
]
