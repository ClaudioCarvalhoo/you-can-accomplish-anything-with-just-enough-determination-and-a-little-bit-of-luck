# Toeplitz Matrix
# A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element.
# Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix.
# The matrix can be any dimensions, not necessarily square.

# For example,
# [[1,2,3,4],
#  [5,1,2,3],
#  [6,5,1,2]]
# is a Toeplitz matrix, so we should return true, while
# [[1,2,3,4],
#  [5,1,9,3],
#  [6,5,1,2]]
# isn’t a Toeplitz matrix, so we should return false.

# O(n * m)
# n = len(arr) | m = len(arr[0])


def isToeplitz(arr):
    if not arr:
        return True

    for i in range(len(arr[0])):
        value = arr[0][i]
        x = i
        y = 0
        while y < len(arr) and x < len(arr[y]):
            if arr[y][x] != value:
                return False
            y += 1
            x += 1

    for i in range(len(arr)):
        value = arr[i][0]
        x = 0
        y = i
        while y < len(arr) and x < len(arr[y]):
            if arr[y][x] != value:
                return False
            y += 1
            x += 1

    return True
