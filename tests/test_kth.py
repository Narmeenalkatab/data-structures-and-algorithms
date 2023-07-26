from scripts.kth import LinkedList
import unittest

class LinkedListTests(unittest.TestCase):
    def test_kth_from_end_greater_than_length(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        self.assertEqual(linked_list.kth_from_end(4), None)

    def test_kth_from_end_same_as_length(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.kth_from_end(3), 1)

    def test_kth_from_end_negative_integer(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.kth_from_end(-1), None)

    def test_kth_from_end_single_node_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        self.assertEqual(linked_list.kth_from_end(0), 1)

    def test_kth_from_end_middle_of_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        self.assertEqual(linked_list.kth_from_end(2), 3)

    def test_kth_from_end_happy_path(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        self.assertEqual(linked_list.kth_from_end(3), 2)

if __name__ == '__main__':
    unittest.main()

           #Stretch Goal test
def test_find_middle():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    middle_node_value = linked_list.find_middle()
    expected_value = 3

    assert middle_node_value == expected_value

test_find_middle()
