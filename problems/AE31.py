# First Duplicate Value

# O(n) time | O(1) space
# n = len(array)


def firstDuplicateValue(array):
    for i in range(len(array)):
        value = abs(array[i])
        position = value - 1
        if array[position] < 0:
            return value
        else:
            mark(array, position)
    return -1


def mark(array, i):
    array[i] *= -1
