import pytest
from scripts.Mergesort import mergesort

def test_mergesort():
    #  array of positive and negative integers
    input_array = [38, 27, 43, 3, 9, 82, -10, -55]

    # Sorting the input array
    sorted_array = mergesort(input_array)

    #  output
    expected_output = [-55, -10, 3, 9, 27, 38, 43, 82]

    assert sorted_array == expected_output

    #  empty array
    empty_array = []
    assert mergesort(empty_array) == []

    #  a single element array
    single_element_array = [42]
    assert mergesort(single_element_array) == [42]

    #  duplicate elements
    duplicate_array = [5, 2, 1, 2, 4, 1, 3]
    assert mergesort(duplicate_array) == [1, 1, 2, 2, 3, 4, 5]

    #  already sorted array
    sorted_array = [1, 2, 3, 4, 5]
    assert mergesort(sorted_array) == [1, 2, 3, 4, 5]

    #  reverse sorted array
    reverse_sorted_array = [5, 4, 3, 2, 1]
    assert mergesort(reverse_sorted_array) == [1, 2, 3, 4, 5]

    #large array
    large_array = list(range(10000, 0, -1))
    assert mergesort(large_array) == list(range(1, 10001))

if __name__ == "__main__":
    pytest.main()
