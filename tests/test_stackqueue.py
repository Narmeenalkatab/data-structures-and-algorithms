import unittest
from scripts.stackqueue import Stack, Queue



class StackTests(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)

    def test_push_multiple_values(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.peek(), 30)

    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)

    def test_empty_stack_after_multiple_pops(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.peek(), 30)

    def test_instantiate_empty_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_pop_on_empty_stack_raises_exception(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.pop()

    def test_peek_on_empty_stack_raises_exception(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.peek()


class QueueTests(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(10)
        self.assertEqual(queue.peek(), 10)

    def test_enqueue_multiple_values(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.peek(), 10)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)

    def test_peek(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.peek(), 10)

    def test_empty_queue_after_multiple_dequeues(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_instantiate_empty_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_dequeue_on_empty_queue_raises_exception(self):
        queue = Queue()
        with self.assertRaises(Exception):
            queue.dequeue()

    def test_peek_on_empty_queue_raises_exception(self):
        queue = Queue()
        with self.assertRaises(Exception):
            queue.peek()


if __name__ == '__main__':
    unittest.main()