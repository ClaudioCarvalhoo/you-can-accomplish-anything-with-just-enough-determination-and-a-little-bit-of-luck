# O(n)
# n = len(nums)


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        largestIndex = max(0, 1, key=lambda x: nums[x])
        secondIndex = min(0, 1, key=lambda x: nums[x])

        for i in range(2, len(nums)):
            if nums[i] > nums[largestIndex]:
                secondIndex = largestIndex
                largestIndex = i
            elif nums[i] > nums[secondIndex]:
                secondIndex = i

        if nums[largestIndex] >= nums[secondIndex] * 2:
            return largestIndex
        else:
            return -1