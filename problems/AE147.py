# Merge Sort

# O(n*log(n))
# n = len(array)


def mergeSort(array):
    return aux(array, 0, len(array) - 1)


def aux(array, start, end):
    if start == end:
        return [array[start]]
    midpoint = start + ((end - start) // 2)
    left = aux(array, start, midpoint)
    right = aux(array, midpoint + 1, end)
    return merge(left, right)


def merge(arr1, arr2):
    p1 = 0
    p2 = 0
    res = []
    while p1 < len(arr1) or p2 < len(arr2):
        if p1 >= len(arr1):
            res.append(arr2[p2])
            p2 += 1
        elif p2 >= len(arr2):
            res.append(arr1[p1])
            p1 += 1
        else:
            if arr1[p1] <= arr2[p2]:
                res.append(arr1[p1])
                p1 += 1
            else:
                res.append(arr2[p2])
                p2 += 1
    return res
