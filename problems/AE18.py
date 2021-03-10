# Insertion Sort

# O(n²)
# n = len(array)


def insertionSort(array):
    for i in range(len(array)):
        cur = i
        for j in range(i - 1, -1, -1):
            if array[cur] < array[j]:
                swap(array, cur, j)
                cur -= 1
    return array


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
