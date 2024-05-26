from django.template.defaulttags import register

@register.filter
def get_submission_score(problem, user):
    score = user.submissions.filter(problem=problem).order_by('-score').first()
    return score or "..."
