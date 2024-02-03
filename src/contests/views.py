from django.shortcuts import render
from django.views.generic import ListView

from contests.models import Contest


class Contests(ListView):
    model = Contest
    context_object_name = "contests"
    template_name = "contests/contests.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["running_contests"] = self.model.objects.filter(is_active=True)
        context["done_contests"] = self.model.objects.filter(is_active=False)
        return context
