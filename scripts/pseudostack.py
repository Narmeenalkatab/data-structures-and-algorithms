class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")


class PseudoQueue:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def enqueue(self, value):
        self.input_stack.push(value)

    def dequeue(self):
        if self.output_stack.is_empty():
            if self.input_stack.is_empty():
                raise IndexError("PseudoQueue is empty")
            else:
                while not self.input_stack.is_empty():
                    self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()

