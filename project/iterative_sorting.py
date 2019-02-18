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
            # if the second element is less than the first, swap
            if arr[i] < arr[j]:
                print(arr)
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
