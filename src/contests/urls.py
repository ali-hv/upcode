from django.urls import path

from .views import Contests, ContestPage, ContestProblems

app_name = "contests"

urlpatterns = [
    path("", Contests.as_view(), name="contests"),
    path("<pk>", ContestPage.as_view(), name="contest_page"),
    path("<pk>/problemset/", ContestProblems.as_view(), name="contest_problems"),
]
