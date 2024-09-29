def add_student(database: dict, student: str):
    database[student] = []
    return database

def print_student(database: dict, student: str):
    if student not in database:
        print(f"{student}: no such person in the database")
    else:
        courses = database[student]
        print(f"{student}:")
        if not courses:
            print(f" no completed courses")
        else:
            average = sum(grade for _, grade in courses) / len(courses)
            print(f" {len(courses)} completed courses:")
            for course, grade in courses:
                print(f"  {course} {grade}")
            print(f" average grade {average:.1f}")

def add_course(database: dict, student: str, course: tuple):
    course_name, grade = course

    if grade == 0:  # ignore grade 0 courses
        return

    for i, (existing_course, existing_grade) in enumerate(database[student]):
        if existing_course == course_name:
            if existing_grade < grade:  # only update if the new grade is higher
                database[student][i] = (course_name, grade)
            return

    database[student].append(course)
    database[student].sort(reverse=True)

def summary(database: dict):
    total_students = len(database)
    most_courses_student = max(database, key=lambda s: len(database[s]), default="")
    most_courses_count = len(database[most_courses_student]) if most_courses_student else 0

    best_average_student = max(
        (s for s in database if database[s]),
        key=lambda s: sum(grade for _, grade in database[s]) / len(database[s]),
        default=""
    )
    best_average = (
        sum(grade for _, grade in database[best_average_student]) / len(database[best_average_student])
        if best_average_student else 0
    )

    print(f"students {total_students}")
    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_average:.1f} {best_average_student}")
