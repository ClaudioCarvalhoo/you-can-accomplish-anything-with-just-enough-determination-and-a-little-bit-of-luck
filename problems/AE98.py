# Sort K-Sorted Array

# O(n*log(k))
# n = len(array) | k = k

import heapq


def sortKSortedArray(array, k):
    heap = []
    for i in range(k + 1):
        if i < len(array):
            heapq.heappush(heap, array[i])

    res = []
    for i in range(len(array)):
        res.append(heapq.heappop(heap))
        if i + k + 1 < len(array):
            heapq.heappush(heap, array[i + k + 1])
    return res
