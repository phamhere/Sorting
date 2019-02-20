# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr

# TO-DO: implement the Quick Sort function below USING RECURSION


def quick_sort(arr, low, high):
    # edge case where length of arr is 0
    if len(arr) == 0:
        return arr
    # making pivot to compare LHS and RHS
    pivot = arr[0]
    # making LHS and RHS lists to append values to later
    LHS = []
    RHS = []
    # looping through arr and appending values to LHS or RHS if <= or > pivot
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            LHS.append(arr[i])
        else:
            RHS.append(arr[i])
    # if length of LHS > 1, recursive call quick_sort
    if len(LHS) > 1:
        LHS = quick_sort(LHS, 0, len(LHS) - 1)
    # if length of RHS > 1, recursive call quick_sort
    if len(RHS) > 1:
        RHS = quick_sort(RHS, 0, len(RHS) - 1)
    # return the separated lists together as one
    return LHS + [pivot] + RHS

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
