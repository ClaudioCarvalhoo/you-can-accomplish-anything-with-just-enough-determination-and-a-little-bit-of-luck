# Search For Range

# O(log(n))
# n = len(array)


def searchForRange(array, target):
    return [searchForLeftmost(array, target), searchForRightmost(array, target)]


def searchForLeftmost(array, target):
    start = 0
    end = len(array)
    while start < end:
        midpoint = start + ((end - start) // 2)
        if array[midpoint] == target and (
            midpoint == 0 or array[midpoint - 1] != target
        ):
            return midpoint
        elif array[midpoint] >= target:
            end = midpoint
        else:
            start = midpoint + 1
    return -1


def searchForRightmost(array, target):
    start = 0
    end = len(array)
    while start < end:
        midpoint = start + ((end - start) // 2)
        if array[midpoint] == target and (
            midpoint == len(array) - 1 or array[midpoint + 1] != target
        ):
            return midpoint
        elif array[midpoint] > target:
            end = midpoint
        else:
            start = midpoint + 1
    return -1
