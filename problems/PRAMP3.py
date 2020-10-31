# Array Quadruplet
# Given an unsorted array of integers arr and a number s,
# write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr
# that sum up to s. Your function should return an array of these numbers in an ascending order.
# If such a quadruplet doesn’t exist, return an empty array.

# Note that there may be more than one quadruplet in arr whose sum is s.
# You’re asked to return the first one you encounter (considering the results are sorted).

# Explain and code the most efficient solution possible, and analyze its time and space complexities.

# Example:

# input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

# Example:
# output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
#                      # whose sum is 20. Notice that there
#                      # are two other quadruplets whose sum is 20:
#                      # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
#                      # asked to return the just one quadruplet (in an
#                      # ascending order)

# Time
# O(n³)
# n = len(arr)

# Space
# O(n)
# n = len(arr)

import collections


def find_array_quadruplet(arr, s):
    arr.sort()
    if len(arr) == 0:
        return []

    table = collections.Counter(arr)

    res = []
    for i1 in range(len(arr)):
        table[arr[i1]] -= 1
        for i2 in range(i1 + 1, len(arr)):
            table[arr[i2]] -= 1
            for i3 in range(i2 + 1, len(arr)):
                table[arr[i3]] -= 1
                res = [arr[i1], arr[i2], arr[i3]]
                need = s - sum(res)
                if need in table and table[need] > 0:
                    res.append(need)
                    return sorted(res)
                table[arr[i3]] += 1
            table[arr[i2]] += 1
        table[arr[i1]] += 1

    return []
