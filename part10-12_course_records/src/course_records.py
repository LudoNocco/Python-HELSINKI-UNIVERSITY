class StudyTracker:
    def __init__(self):
        self.courses = {}

    def add_course(self, course, grade, credits):
        if course not in self.courses or self.courses[course]['grade'] < grade:
            self.courses[course] = {'grade': grade, 'credits': credits}

    def get_course_data(self, course):
        if course in self.courses:
            data = self.courses[course]
            print(f"{course} ({data['credits']} cr) grade {data['grade']}")
        else:
            print("no entry for this course")

    def statistics(self):
        if not self.courses:
            print("no courses added yet")
            return

        total_credits = sum(course['credits'] for course in self.courses.values())
        total_courses = len(self.courses)
        mean_grade = sum(course['grade'] for course in self.courses.values()) / total_courses

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")

        grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.courses.values():
            grade_distribution[course['grade']] += 1

        for grade in sorted(grade_distribution.keys(), reverse=True):
            print(f"{grade}: {'x' * grade_distribution[grade]}")

tracker = StudyTracker()

while True:
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
    command = input("command: ")

    if command == "1":
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        tracker.add_course(course, grade, credits)

    elif command == "2":
        course = input("course: ")
        tracker.get_course_data(course)

    elif command == "3":
        tracker.statistics()

    elif command == "0":
        break
