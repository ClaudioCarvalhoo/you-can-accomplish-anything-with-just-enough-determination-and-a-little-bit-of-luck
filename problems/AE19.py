# Selection Sort

# O(n²)
# n = len(array)


def selectionSort(array):
    for i in range(len(array)):
        smallestIndex = i
        for j in range(i, len(array)):
            smallestIndex = j if array[j] < array[smallestIndex] else smallestIndex
        swap(array, i, smallestIndex)
    return array


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
