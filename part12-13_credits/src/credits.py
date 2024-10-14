from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda total, attempt: total + attempt.credits, passed_attempts, 0)

def average(attempts: list):
    passed_attempts = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    
    if len(passed_attempts) == 0:
        return 0

    total_grade = reduce(lambda total, attempt: total + attempt.grade, passed_attempts, 0)
    
    return total_grade / len(passed_attempts)
