# O(n)
# n = len(nums)

from typing import List

# Normal solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

        for i in table.keys():
            if table[i] == 1:
                return i


# This has O(1) space complexity
# Xor between a number and itself = 0
# Xor between 0 and n = n
# All numbers cancell eachother until only n remains in the end
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res