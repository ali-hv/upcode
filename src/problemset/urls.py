from django.urls import path

from .views import Problemset

app_name = "problemset"

urlpatterns = [
    path("", Problemset.as_view(), name="problemset"),
]
