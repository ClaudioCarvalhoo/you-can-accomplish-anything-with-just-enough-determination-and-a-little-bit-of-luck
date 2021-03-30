# Largest Range

# O(n)
# n = len(array)


def largestRange(array):
    ranges = {}
    existing = set(array)

    bestRangeStart = array[0]
    bestRangeLength = 1
    for num in array:
        rangeSize = explore(num, ranges, existing)
        if rangeSize >= bestRangeLength:
            bestRangeStart = num
            bestRangeLength = rangeSize
    return [bestRangeStart, bestRangeStart + bestRangeLength - 1]


def explore(num, ranges, existing):
    if num not in existing:
        return 0
    if num not in ranges:
        ranges[num] = 1 + explore(num + 1, ranges, existing)
    return ranges[num]
