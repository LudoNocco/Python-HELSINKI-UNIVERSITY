class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    return [submission for submission in submissions if submission.points >= lowest_passing]
