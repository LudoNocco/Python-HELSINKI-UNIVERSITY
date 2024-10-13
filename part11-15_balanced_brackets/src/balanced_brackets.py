def balanced_brackets(my_string: str):
    def helper(s, index, stack):
        if index == len(s):
            return len(stack) == 0
        char = s[index]
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack:
                return False
            open_bracket = stack.pop()
            if (open_bracket == '(' and char != ')') or (open_bracket == '[' and char != ']'):
                return False
        return helper(s, index + 1, stack)
    
    brackets_only = [char for char in my_string if char in '()[]']
    return helper(brackets_only, 0, [])