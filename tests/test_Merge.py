import pytest
from test.Merge import merge_sort 
def test_merge_sort():
    arr = [8, 4, 23, 42, 16, 15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

    arr = [20, 18, 12, 8, 5, -2]
    merge_sort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

    arr = [5, 12, 7, 5, 5, 7]
    merge_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

    arr = [2, 3, 5, 7, 13, 11]
    merge_sort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

    arr = []
    merge_sort(arr)
    assert arr == []

    arr = [42]
    merge_sort(arr)
    assert arr == [42]

    arr = [3, 2, 2, 1, 3, 1, 2]
    merge_sort(arr)
    assert arr == [1, 1, 2, 2, 2, 3, 3]

if __name__ == '__main__':
    pytest.main()
