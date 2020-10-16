# O(n)
# n = len(nums)

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        table = {}
        twice = -1
        nums_sum = 0
        expected_sum = 0
        for i in range(len(nums)):
            expected_sum += i + 1
            if nums[i] in table:
                twice = nums[i]
            else:
                table[nums[i]] = True
                nums_sum += nums[i]

        return [twice, expected_sum - nums_sum]