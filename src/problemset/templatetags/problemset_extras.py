from django.template.defaulttags import register
import re


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


@register.filter
def to_persian(date):
    num_word = {'01': 'فروردین', '02': 'اردیبهشت', '03': 'خرداد', '04': 'تیر', '05': 'مرداد', '06': 'شهریور',
                '07': 'مهر', '08': 'آبان', '09': 'آذر', '10': 'دی', '11': 'بهمن', '12': 'اسفند'}

    farsi_nums = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}

    date = date.split('/')

    if '-' in date[2]:
        date.append(None)
        date[3] = date[2].split('-')[1].strip() + ' - '
        date[2] = date[2].split('-')[0].strip()

    date[1] = num_word[date[1]]
    date[2] = re.sub(r'0(\d)', r'\1', date[2])
    date.reverse()
    date = ' '.join(date)

    for i in farsi_nums:
        date = date.replace(i, farsi_nums[i])

    return date
