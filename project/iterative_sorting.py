# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    # loop through elements in arr starting with the second element
    for i in range(1, len(arr)):
        # loop backwards starting from i-1 to 0
        for j in range(i-1, -1, -1):
            print(arr[i], arr[j])
            # if the second element is less than the first, swap
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
    return arr

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    # iterating through length of arr
    for i in range(len(arr)):
        """iterating through length of arr minus one since checking the j+1 element
        and minus i since the end elements are already sorted"""
        for j in range(len(arr) - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
