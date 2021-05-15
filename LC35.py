# O(n)
# n = len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        midpoint = 0
        while start < end:
            midpoint = start + ((end - start) // 2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
            else:
                end = midpoint

        if target < nums[midpoint]:
            return midpoint
        else:
            return midpoint + 1