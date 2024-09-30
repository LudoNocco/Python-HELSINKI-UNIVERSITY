from datetime import datetime, timedelta

def final_points():
    start_times = {}
    student_scores = {}

    with open('start_times.csv', 'r') as file:
        for line in file:
            name, time_str = line.strip().split(';')
            start_times[name] = datetime.strptime(time_str, '%H:%M')

    with open('submissions.csv', 'r') as file:
        for line in file:
            name, task_str, points_str, submit_time_str = line.strip().split(';')
            task = int(task_str)
            points = int(points_str)
            submit_time = datetime.strptime(submit_time_str, '%H:%M')
            if name in start_times:
                start_time = start_times[name]
                time_diff = submit_time - start_time
                if time_diff <= timedelta(hours=3):
                    if name not in student_scores:
                        student_scores[name] = {}
                    if task not in student_scores[name] or points > student_scores[name][task]:
                        student_scores[name][task] = points

    final_scores = {}
    for name, tasks in student_scores.items():
        total_points = sum(tasks.values())
        final_scores[name] = total_points

    return final_scores
