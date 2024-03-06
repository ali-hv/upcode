from django.urls import path

from .views import Problemset, ProblemPage, CreateSubmission

app_name = "problemset"

urlpatterns = [
    path("", Problemset.as_view(), name="problemset"),
    path("<pk>", ProblemPage.as_view(), name="problem_page"),
    path("create_submission/", CreateSubmission.as_view(), name="create_submission"),
]
