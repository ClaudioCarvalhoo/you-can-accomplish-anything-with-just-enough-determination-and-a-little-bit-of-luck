# Radix Sort

# O(n*l)
# n = len(array) | l = maxLen(array)

import math


def radixSort(array):
    if len(array) <= 0:
        return []

    maxLen = max([getNumberLength(num) for num in array])
    return helper(array, 0, maxLen)


def helper(array, pos, maxLen):
    if len(array) <= 1 or pos > maxLen:
        return array

    buckets = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for num in array:
        buckets[getDigitAtPos(num, pos, maxLen)].append(num)

    res = []
    for i in range(10):
        res += helper(buckets[i], pos + 1, maxLen)
    return res


def getNumberLength(num):
    if num == 0:
        return 1
    return int(math.log10(num)) + 1


def getDigitAtPos(num, pos, maxLen):
    if getNumberLength(num) < maxLen - pos:
        return 0
    else:
        return (num // (10 ** (maxLen - pos))) % 10
