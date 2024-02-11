from subprocess import Popen, PIPE, TimeoutExpired
import os

from django.core.files import File


def judge_python(submission):
    score = 0

    result_filename = f"{submission.id}-{submission.user_id}-result.txt"
    result = open(result_filename, "w").close()

    for test_case in submission.problem.test_cases.all():
        # Read input from file
        with open(test_case.input_file.path, "r") as f:
            input_content = f.read().strip().split("\n")

        user_file = submission.file.path

        # Run the main program and capture output
        process = Popen(
            ["python", user_file],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
        )

        memory_limit = submission.problem.memory_limit

        # TODO resource lib only works in unix based operating systems(install in the docker)
        # resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))

        # Read expected output from output1.txt
        with open(test_case.output_file.path, "r") as f:
            expected_output = f.read().strip().split("\n")

        try:
            output, _ = process.communicate("\n".join(input_content), timeout=submission.problem.time_limit)

            # Compare output with expected output
            if output.strip().split("\n") == expected_output:
                with open(result_filename, 'a') as f:
                    f.write("Accepted\n")
                score += 1
            else:
                with open(result_filename, 'a') as f:
                    f.write("Wrong Answer\n")
        except TimeoutExpired:
            with open(result_filename, 'a') as f:
                f.write("Time Limit Exceeded\n")
        except MemoryError:
            with open(result_filename, "a") as f:
                f.write("Memory Limit Exceeded\n")

    submission.score = score / len(submission.problem.test_cases.all()) * 100
    submission.save()

    with open(result_filename, 'rb') as file:
        file = File(file)
        submission.result.save(os.path.basename(result_filename), file)

    os.remove(result_filename)
