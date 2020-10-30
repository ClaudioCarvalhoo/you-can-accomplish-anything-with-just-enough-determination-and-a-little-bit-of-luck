# O(n) time
# O(1) space (excluding output space)
# n = len(nums)
# Question specifically asked not to use any divisions

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        soFar = 1
        for i in range(len(nums)):
            res.append(soFar)
            soFar *= nums[i]

        soFar = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= soFar
            soFar *= nums[i]

        return res