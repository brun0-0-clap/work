from merge_sort import merge_sort

def test_sort_random():
    arr = [9, 2, 5, 1, 7]
    assert merge_sort(arr) == [1, 2, 5, 7, 9]

def test_sort_sorted():
    arr = [1,2,3,4,5]
    assert merge_sort(arr) == [1,2,3,4,5]
