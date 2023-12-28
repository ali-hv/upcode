from django.template.defaulttags import register


@register.filter
def is_solved(problem, user):
    for i in problem:
        if i.user == user:
            if i.status == "solved":
                return True
    else:
        return False


@register.filter
def is_partial(problems, user):
    for i in problems:
        if i.user == user:
            if i.status == "partial":
                return True
    else:
        return False
