import unittest
from scripts.merge27 import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        merge_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 3]
        merge_sort(arr)
        self.assertEqual(arr, [2, 2, 3, 5, 5, 8])

    def test_negative_elements(self):
        arr = [-5, -2, -8, -1, -3]
        merge_sort(arr)
        self.assertEqual(arr, [-8, -5, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()
