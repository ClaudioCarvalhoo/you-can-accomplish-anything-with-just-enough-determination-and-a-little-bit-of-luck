# O(log(n))
# n = len(arr)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)
        while start < end:
            midpoint = start + ((end - start) // 2)
            if arr[midpoint] > arr[midpoint - 1] and arr[midpoint] > arr[midpoint + 1]:
                return midpoint
            elif arr[midpoint] < arr[midpoint - 1]:
                end = midpoint
            else:
                start = midpoint + 1