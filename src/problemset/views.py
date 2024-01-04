from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from contests.models import Contest
from .models import Problem, Tag, Submission, Language


class Problemset(ListView):
    model = Problem
    queryset = model.objects.all()
    context_object_name = "problemset"
    template_name = "problemset/problemset.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["contests"] = Contest.objects.all()
        return context


class ProblemPage(DetailView):
    model = Problem
    context_object_name = "problem"
    template_name = "problemset/problem.html"


class CreateSubmission(View):
    def post(self, request):
        language_name = request.POST.get("language")
        language_id = get_object_or_404(Language, name=language_name).id

        obj = Submission(
            user=request.user,
            file=request.FILES["submission-file"],
            problem_id=request.POST.get("problem"),
            language_id=language_id,
        )
        obj.save()

        return redirect(reverse("problemset:problem_page", args=[request.POST.get("problem")])+"?tab=submission")
