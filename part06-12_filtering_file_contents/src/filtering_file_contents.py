import os

def filter_solutions():
    correct_solutions = []
    incorrect_solutions = []

    # Read the solutions.csv file
    with open('solutions.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        name, problem, result = line.strip().split(';')
        result = int(result)

        if '+' in problem:
            operands = problem.split('+')
            calculated_result = int(operands[0]) + int(operands[1])
        elif '-' in problem:
            operands = problem.split('-')
            calculated_result = int(operands[0]) - int(operands[1])

        if calculated_result == result:
            correct_solutions.append(line)
        else:
            incorrect_solutions.append(line)

    with open('correct.csv', 'w') as correct_file:
        correct_file.writelines(correct_solutions)

    with open('incorrect.csv', 'w') as incorrect_file:
        incorrect_file.writelines(incorrect_solutions)