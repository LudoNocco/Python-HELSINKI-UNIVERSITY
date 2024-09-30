def read_file(file_name):
    file_name_lower = file_name.lower()
    with open(file_name) as file:
        if any(keyword in file_name_lower for keyword in ['students', 'exercises', 'exam_points']):
            data = {}
            for line in file:
                line = line.strip()
                parts = line.split(';')
                if parts[0] == 'id':
                    continue
                data[parts[0]] = parts[1:]
            return data
        elif 'course' in file_name_lower:
            course_info = []
            for line in file:
                line = line.strip()
                parts = line.split(':')
                course_info.append(parts[1].strip())
            return course_info

def convert_values_to_int(data_dict):
    for key in data_dict:
        data_dict[key] = [int(value) for value in data_dict[key]]

def points_to_grade(points):
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5

def write_results(students, exercises, exams, course, results_file_name):
    header = f"{course[0]}, {course[1]} credits\n" + "=" * 38 + "\n"
    header += f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"
    report = header
    students_grade = []
    for id_, name in students.items():
        exercise_total = sum(exercises[id_])
        exercise_points = int((exercise_total / 40) * 10)
        exam_points = sum(exams[id_])
        total_points = exercise_points + exam_points
        grade = points_to_grade(total_points)
        full_name = f"{name[0]} {name[1]}"
        students_grade.append([id_, full_name, str(grade)])
        report += f"{full_name:30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}\n"

    with open(f"{results_file_name}.txt", 'w') as txt_file:
        txt_file.write(report)
    with open(f"{results_file_name}.csv", 'w') as csv_file:
        for record in students_grade:
            csv_file.write(';'.join(record) + '\n')
    print(f"Results written to files {results_file_name}.txt and {results_file_name}.csv")

def main():
    student_file = input('Student information: ')
    exercises_file = input('Exercises completed: ')
    exam_file = input('Exam points: ')
    course_file = input('Course information: ')
    results_file = 'results'

    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)
    course = read_file(course_file)

    convert_values_to_int(exercises)
    convert_values_to_int(exams)

    write_results(students, exercises, exams, course, results_file)

main()
