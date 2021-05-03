# Index Equals Value

# O(log(n))
# n = len(array)


def indexEqualsValue(array):
    start = 0
    end = len(array)
    while start < end:
        midpoint = start + ((end - start) // 2)
        if array[midpoint] == midpoint and (
            midpoint == 0 or array[midpoint - 1] != midpoint - 1
        ):
            return midpoint
        elif array[midpoint] < midpoint:
            start = midpoint + 1
        else:
            end = midpoint
    return -1
