from insertionsort import insertion_sort
import pytest


def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

def test_insertion_sort():
    # Test case 1
    sample_array = [8, 4, 23, 42, 16, 15]
    sorted_array = insertion_sort(sample_array)
    assert sorted_array == [4, 8, 15, 16, 23, 42]

    # Test case 2
    sample_array = [20, 18, 12, 8, 5, -2]
    sorted_array = insertion_sort(sample_array)
    assert sorted_array == [-2, 5, 8, 12, 18, 20]

    # Test case 3
    sample_array = [5, 12, 7, 5, 5, 7]
    sorted_array = insertion_sort(sample_array)
    assert sorted_array == [5, 5, 5, 7, 7, 12]

    # Test case 4
    sample_array = [2, 3, 5, 7, 13, 11]
    sorted_array = insertion_sort(sample_array)
    assert sorted_array == [2, 3, 5, 7, 11, 13]

    print("All test cases pass")

# Run the test function
test_insertion_sort()
