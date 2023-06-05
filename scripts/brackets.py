


def validate_brackets(string):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
