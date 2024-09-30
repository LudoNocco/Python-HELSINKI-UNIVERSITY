from datetime import datetime, timedelta

def cheaters():
    start_times = {}
    cheaters_set = set()

    # Read start_times.csv
    with open('start_times.csv', 'r') as file:
        for line in file:
            name, time_str = line.strip().split(';')
            start_times[name] = datetime.strptime(time_str, '%H:%M')

    # Read submissions.csv
    with open('submissions.csv', 'r') as file:
        for line in file:
            name, task, points, submit_time_str = line.strip().split(';')
            submit_time = datetime.strptime(submit_time_str, '%H:%M')
            if name in start_times:
                start_time = start_times[name]
                time_diff = submit_time - start_time
                if time_diff > timedelta(hours=3):
                    cheaters_set.add(name)

    return list(cheaters_set)
