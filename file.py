"""Sorting algorithms for lists that contain integer values."""

from typing import List

from random import randint

# Reference for some algorithm implementations:
# https://realpython.com/sorting-algorithms-python/

# TODO: Add all of the source code based on the above article

# TODO: Please develop an intuitive understanding about which of
# these sorting algorithms are fast and which ones are slow. To
# build up this intuitive understand you can read additional
# online articles, check your course text book, and count
# the number of iteration constructs and basic operations.

# Make sure that you add comments to all of these functions
# so as to make it clear that you understand how each step works


def bubble_sort(array: List[int]) -> List[int]:
    """Sort an input list called array using bubble sort."""
    n = len(array)
    for i in range(n):
        # creating a flag a that will allow function
        # to terminate eaely if nothing to sort
        already_sorted = True
        # start to look at each item one by one, comparing with adjecent value
        # with every iteration, the portion of array is shrinking
        # beacuse the remainng items alredy sorted
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
            # if item we looking at greater than its adjacent value, swap
                array[j], array[j + 1] = array[j + 1], array[j]
            # since we swapped two elements
            # set already_sorted flag to false so
            # that algorithm doesnt finish prematurely
            already_sorted = False
        if already_sorted:
            break
        return array

def insertion_sort(array: List[int]) -> List[int]:
    """Run an insertion sort on the provided array."""
    # loop for seconf element until last element
    for i in range(1, len(array)):
        # element we want to position in correct place
        key_item = array[i]
        # initialize the variabe that eill be used to
        # find the correct position of the element referenced by key_item
        j = i - 1
        # run through lsit of items(left portion of array)
        # find correct position of the element referenced by key_item.
        # do this only if key_item is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # shift value one position to the left
            # and reposition j to the next element
            # (from left to right)
            array[j + 1] = array[j]
            j -= 1
        # When finish shifting elements, you can position
        # keu_item in its correct location
        array[j + 1] = key_item
    return array


def merge(left: List[int], right: List[int]) -> List[int]:
    """Define a convenience method that supports the merging of lists."""
# If first array empty, no need to merge,
# return second array as the result
    if len(left) == 0:
        return right
# if second array empty, no need merge, return first array
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
# go through both array until all elements make it into result array
    while len(result) < len(left) + len(right):
       # elements need to be sorted to add them to result array,
       # need to decide whether to get next elemet from the first or second array 
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        # if reach end of either array, add remaing elemetns from
        # the otehr array to the result and break loop
        if index_right == len(right):
            result += left[index_left]
            break
        if index_left == len(left):
            result+= right[index_right]
            break
    return result


def merge_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the merge sort algorithm."""
    # if input array contains less than 2 elements,
    # return is as the result
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    # sort array by recursively splitting the input,
    # into equal halves, sorting each half and merging them into final result
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))

def quick_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the quick sort algorithm."""
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        # elements smaller than than `pivot`go to low list,
        # elements larger than pivot go the `high` list
        # elements equal to pivot go to the `same` list
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quick_sort(low) + same + quick_sort(high)


def insertion_sort_tim(array: List[int], left: int = 0, right=None):
    """Use an internal sorting algorithm for the timsort algorithm."""
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def tim_sort(array: List[int]) -> List[int]:
    """Sort the list called array with the tim sort algorithm using a special insertion sort."""
    sorted_runs = []
    runs = []
    length = len(array)
    new_run = [array[0]]

    # for every i in the range of 1 to length of array
    for i in range(1, length):
        # if i is at the end of the list
        if i == length - 1:
            new_run.append(array[i])
            runs.append(new_run)
            break
        # if the i'th element of the array is less than the one before it
        if array[i] < array[i-1]:
            # if new_run is set to None (NULL)
            if not new_run:
                runs.append([array[i]])
                new_run.append(array[i])
            else:
                runs.append(new_run)
                new_run = []
        # else if its equal to or more than
        else:
            new_run.append(array[i])

    # for every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    
    # for every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)