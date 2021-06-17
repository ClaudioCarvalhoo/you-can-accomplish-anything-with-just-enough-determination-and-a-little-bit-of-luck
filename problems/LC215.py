# Average Case: O(n)
# Worst Case: O(n²)
# n = len(nums)

import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        pivotIndex = random.randint(start, end)
        self.swap(nums, pivotIndex, end)
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] >= pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, end, i)
        if i == k - 1:
            return pivot
        elif i > k - 1:
            return self.quickSelect(nums, start, i - 1, k)
        else:
            return self.quickSelect(nums, i + 1, end, k)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]