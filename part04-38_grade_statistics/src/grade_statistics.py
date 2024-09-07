def calculate_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points

    if exam_points < 10:
        return 0
    if total_points >= 28:
        return 5
    elif total_points >= 24:
        return 4
    elif total_points >= 21:
        return 3
    elif total_points >= 18:
        return 2
    elif total_points >= 15:
        return 1
    else:
        return 0

def process_input():
    results = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if not user_input:  
            break
        exam_points, exercises_completed = map(int, user_input.split())
        exercise_points = exercises_completed // 10  
        grade = calculate_grade(exam_points, exercise_points)
        results.append((exam_points, exercise_points, grade))
    
    return results

def print_statistics(results):
    if not results:
        print("No data entered.")
        return
    
    total_points = [exam + exercise for exam, exercise, _ in results]
    total_passed = [1 for exam, exercise, grade in results if grade > 0]
    total_grades = [grade for _, _, grade in results]
    
    # Calculate statistics
    average_points = sum(total_points) / len(results)
    pass_percentage = (len(total_passed) / len(results)) * 100
    
    # Print statistics
    print("Statistics:")
    print(f"Points average: {average_points:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    
    for grade in range(5, -1, -1):
        count = total_grades.count(grade)
        print(f"  {grade}: {'*' * count}")

def main():
    results = process_input()
    print_statistics(results)

main()
