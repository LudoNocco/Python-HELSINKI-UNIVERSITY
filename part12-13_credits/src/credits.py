from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def accepted(attempts: list):
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)

def sum_of_all_credits(attempts: list):
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda total, attempt: total + attempt.credits if attempt.grade > 5 else total, attempts, 0)