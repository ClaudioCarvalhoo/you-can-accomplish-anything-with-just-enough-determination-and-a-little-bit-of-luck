# Shifted Binary Search

# O(log(n))
# n = len(array)


def shiftedBinarySearch(array, target):
    shiftIndex = findShiftIndex(array)

    start = shiftIndex
    end = start + len(array)
    while start < end:
        midpoint = start + ((end - start) // 2)
        trueMidpoint = midpoint % len(array)
        if array[trueMidpoint] == target:
            return trueMidpoint
        if array[trueMidpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint
    return -1


def findShiftIndex(array):
    start = 0
    end = len(array)
    while start < end:
        midpoint = start + ((end - start) // 2)
        if midpoint == 0 or array[midpoint] < array[midpoint - 1]:
            return midpoint
        if array[midpoint] > array[-1]:
            start = midpoint + 1
        else:
            end = midpoint
