from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from contests.models import Contest


class Contests(ListView):
    model = Contest
    context_object_name = "contests"
    template_name = "contests/contests.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["running_contests"] = self.model.objects.filter(end_time__gte=now)
        context["done_contests"] = self.model.objects.filter(end_time__lte=now)
        return context


class ContestPage(DetailView):
    model = Contest
    context_object_name = "contest"
    template_name = "contests/contest_page.html"


class ContestProblems(DetailView):
    model = Contest
    context_object_name = "contest"
    template_name = "contests/contest_problems.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        problem_id = self.kwargs.get('problem_id')
        if problem_id:
            context['problem'] = get_object_or_404(self.object.problems, id=problem_id)
        else:
            context['problem'] = self.object.problems.first()

        return context


class ContestScoreboard(DetailView):
    model = Contest
    template_name = "contests/contest_scoreboard.html"


def register_user_to_contest(request, contest_id):
    contest = Contest.objects.get(pk=contest_id)
    contest.participants.add(request.user)

    return redirect('contests:contests')
