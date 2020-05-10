#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    if item == array[index]:
        return index
    return linear_search_recursive(array, item, index=index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    array.sort()
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        if array[mid] < item:
            left = mid + 1
        if array[mid] > item:
            right = mid - 1
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    array.sort()
    if left is None and right is None:
        left, right = 0, len(array) - 1
    mid = (left + right) // 2
    if left > right:
        return None
    if array[mid] == item:
        return mid
    if array[mid] < item:
        return binary_search_recursive(array, item, left=mid + 1, right=right)
    if array[mid] > item:
        return binary_search_recursive(array, item, left=left, right=mid - 1)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
