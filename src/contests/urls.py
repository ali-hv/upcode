from django.urls import path

from .views import Contests

app_name = "contests"

urlpatterns = [
    path("", Contests.as_view(), name="contests"),
]
