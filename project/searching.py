import math
# STRETCH: implement Linear Search


def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    # TO-DO: add missing code
    while low <= high:
        # recalculates mid of low and high each loop
        mid = math.floor((low+high)/2)
        # if target is less than mid, changes high to mid - 1
        if target < arr[mid]:
            high = mid - 1
        # if target is greater than mid, changes low to mid + 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = math.floor((low+high)/2)

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    elif low > high:
        return -1
    # Basecase where target equals middle, returns to exit out of function
    elif target == arr[middle]:
        return middle
    else:
        if target > arr[middle]:
            binary_search_recursive(arr, target, middle + 1, high)
        elif target < arr[middle]:
            binary_search_recursive(arr, target, low, middle - 1)
