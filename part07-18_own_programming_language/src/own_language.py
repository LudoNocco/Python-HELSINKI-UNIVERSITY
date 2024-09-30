def run(program):
    variables = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    labels = {}
    output = []
    index = 0

    for i, line in enumerate(program):
        line = line.strip()
        if line.endswith(":"):
            label = line[:-1]
            labels[label] = i

    def get_value(val):
        if val in variables:
            return variables[val]
        return int(val)

    def evaluate_condition(left, operator, right):
        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '<=':
            return left <= right
        elif operator == '>':
            return left > right
        elif operator == '>=':
            return left >= right
        else:
            raise ValueError(f"Unknown operator: {operator}")

    while index < len(program):
        line = program[index].strip()
        tokens = line.split()

        if not tokens:
            index += 1
            continue

        cmd = tokens[0]

        if cmd.endswith(":"):
            index += 1
            continue

        elif cmd == 'PRINT':
            output.append(get_value(tokens[1]))
            index += 1

        elif cmd == 'MOV':
            variables[tokens[1]] = get_value(tokens[2])
            index += 1

        elif cmd == 'ADD':
            variables[tokens[1]] += get_value(tokens[2])
            index += 1

        elif cmd == 'SUB':
            variables[tokens[1]] -= get_value(tokens[2])
            index += 1

        elif cmd == 'MUL':
            variables[tokens[1]] *= get_value(tokens[2])
            index += 1

        elif cmd == 'JUMP':
            label = tokens[1]
            index = labels[label]

        elif cmd == 'IF':
            if len(tokens) != 6 or tokens[4] != 'JUMP':
                raise ValueError("Invalid IF statement format")
            left = get_value(tokens[1])
            operator = tokens[2]
            right = get_value(tokens[3])
            label = tokens[5]
            if evaluate_condition(left, operator, right):
                index = labels[label]
            else:
                index += 1

        elif cmd == 'END':
            break

        else:
            raise ValueError(f"Unknown command: {cmd}")

    return output
