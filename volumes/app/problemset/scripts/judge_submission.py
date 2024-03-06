from .languages import python


def judge(submission):
    if str(submission.language) == 'Python3':
        python.judge(submission)
