from subprocess import Popen, PIPE, STDOUT
import sys
import os

from django.core.files import File


def judge_python(submission):
    with open(submission.problem.test_cases.path, 'r') as f:
        test_cases = f.readlines()
    test_cases = [i.strip().split(',') for i in test_cases]

    result_filename = f'{submission.id}-{submission.user_id}-result.txt'
    result = open(result_filename, 'w').close()

    user_file = submission.file.path

    score = 0

    for i in test_cases:
        _input = i[0]
    
        communicate_argument = _input
        p = Popen(
            [sys.executable, user_file],
            stdout=PIPE,
            stdin=PIPE,
            stderr=STDOUT,
            encoding="utf-8",
        )
    
        stdout, stderr = p.communicate(communicate_argument)
    
        try:
            if stdout.strip() == i[1]:
                with open(result_filename, 'a') as f:
                    f.write("Accepted\n")
                score += 1
            else:
                with open(result_filename, 'a') as f:
                    f.write("Wrong Answer\n")
        except RuntimeError:
            with open(result_filename, 'a') as f:
                f.write("Runtime Error\n")

        submission.score = score / len(test_cases) * 100
        submission.save()

    with open(result_filename, 'rb') as file:
        file = File(file)
        submission.result.save(os.path.basename(result_filename), file)

    os.remove(result_filename)
