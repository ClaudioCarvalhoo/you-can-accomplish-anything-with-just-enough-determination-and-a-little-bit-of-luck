# Subarray Sort

# O(n)
# n = len(array)


def subarraySort(array):
    unsortedIndexes = []
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            unsortedIndexes.append(i)
    if len(unsortedIndexes) == 0:
        return [-1, -1]

    start = unsortedIndexes[0]
    end = unsortedIndexes[-1]
    subarrayMax = max(array[start : end + 1])
    subarrayMin = min(array[start : end + 1])

    increasing = True
    while increasing:
        increasing = False
        if start > 0 and array[start - 1] > subarrayMin:
            start -= 1
            subarrayMax = max(subarrayMax, array[start])
            increasing = True
        if end < len(array) - 1 and array[end + 1] < subarrayMax:
            end += 1
            subarrayMin = min(subarrayMin, array[end])
            increasing = True

    return [start, end]
