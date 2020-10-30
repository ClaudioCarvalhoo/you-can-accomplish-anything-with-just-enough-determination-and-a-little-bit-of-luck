# O(n)
# n = len(nums)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = 0
        for i in range(len(nums) + 1):
            expectedSum += i
        actualSum = 0
        for i in nums:
            actualSum += i
        return expectedSum - actualSum