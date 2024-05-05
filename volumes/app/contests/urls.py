from django.urls import path

from .views import Contests, ContestPage, ContestProblems, register_user_to_contest

app_name = "contests"

urlpatterns = [
    path("", Contests.as_view(), name="contests"),
    path("<pk>", ContestPage.as_view(), name="contest_page"),
    path("register-user/<int:contest_id>", register_user_to_contest, name="register_user"),
    path("<pk>/problemset/", ContestProblems.as_view(), name="contest_problems"),
]
