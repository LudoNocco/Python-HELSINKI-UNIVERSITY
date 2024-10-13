class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempted_courses: list):
    return map(lambda x: x.student_name, attempted_courses)

def course_names(attempted_courses: list):
    return map(lambda x: x.course_name, attempted_courses)