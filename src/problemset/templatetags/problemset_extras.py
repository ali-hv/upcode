from django.template.defaulttags import register


@register.filter
def is_solved(problem, user):
    for i in problem:
        if i.user == user and i.status == "solved":
            return True
    return False


@register.filter
def is_partial(problems, user):
    for i in problems:
        if i.user == user and i.status == "partial":
            return True
    return False


@register.filter
def get_submissions(problems, user):
    submissions = []
    for i in problems:
        if i.user == user:
            submissions.append(i)
    return submissions
