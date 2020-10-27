def mergesort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    return merge(mergesort(arr[:midpoint]), mergesort(arr[midpoint:]))


def merge(arr1, arr2):
    res = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) or p2 < len(arr2):
        if p1 >= len(arr1):
            res += arr2[p2:]
            break
        if p2 >= len(arr2):
            res += arr1[p1:]
            break
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    return res
