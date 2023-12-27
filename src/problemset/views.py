from django.views.generic import ListView

from contests.models import Contest
from .models import Problem, Tag


class Problemset(ListView):
    model = Problem
    queryset = model.objects.all()
    context_object_name = "problemset"
    template_name = "problemset/problemset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["contests"] = Contest.objects.all()
        return context
