# O(n) time | O(1) space
# n = len(nums)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] != None:
                pos = nums[i]
                while pos != None and pos > 0 and pos <= len(nums):
                    temp = nums[pos - 1]
                    nums[pos - 1] = None
                    pos = temp

        for i in range(1, len(nums) + 1):
            if nums[i - 1] != None:
                return i
            i += 1
        return len(nums) + 1
