class Stack:
    """Custom implementation of a stack."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None


class Queue:
    """Custom implementation of a queue."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


def validate_brackets(string):
    """Validate if brackets in the string are balanced.

    Args:
        string (str): The string to validate.

    Returns:
        bool: True if brackets are balanced, False otherwise.
    """
    stack = Stack()
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.peek() != bracket_pairs[char]:
                return False
            stack.pop()

    return stack.is_empty()
