from scripts.pseudostack import Stack,PseudoQueue
import unittest


class PseudoQueueTestCase(unittest.TestCase):
    def test_enqueue(self):
        queue = PseudoQueue()
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(15)
        queue.enqueue(20)
        self.assertEqual(queue.input_stack.stack, [5, 10, 15, 20])
        self.assertEqual(queue.output_stack.stack, [])


    def test_dequeue(self):
        queue = PseudoQueue()
        queue.input_stack.stack = [5, 10, 15, 20]
        queue.output_stack.stack = []
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.input_stack.stack, [])
        self.assertEqual(queue.output_stack.stack, [20, 15, 10])
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.input_stack.stack, [])
        self.assertEqual(queue.output_stack.stack, [20, 15])



if __name__ == '__main__':
    unittest.main()
