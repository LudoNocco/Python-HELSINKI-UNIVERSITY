import urllib.request
import json
import certifi

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(address, cafile=certifi.where())
    data = json.loads(response.read())
    
    active_courses = []
    for course in data:
        if course['enabled']:
            course_info = (
                course['fullName'],
                course['name'],
                course['year'],
                sum(course['exercises'])
            )
            active_courses.append(course_info)
    
    return active_courses

def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(address, cafile=certifi.where())
    data = json.loads(response.read())
    
    weeks = len(data)
    students = max(week['students'] for week in data.values())
    hours = sum(week['hour_total'] for week in data.values())
    exercises = sum(week['exercise_total'] for week in data.values())
    hours_average = hours // students
    exercises_average = exercises // students
    
    return {
        'weeks': weeks,
        'students': students,
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
    }
