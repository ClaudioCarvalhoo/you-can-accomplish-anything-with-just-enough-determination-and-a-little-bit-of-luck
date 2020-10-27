def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, -1)
    return quicksort(arr[:i]) + quicksort(arr[i:])


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
