# O(n * log(m))
# n = len(nums) | m = max(nums)

import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        best = max(nums)
        start = 1
        end = best
        while end >= start:
            current = start + int((end - start) / 2)
            result = self.calculateResult(nums, current)
            if result > threshold:
                start = current + 1
            else:
                best = min(best, current)
                end = current - 1
        return best

    def calculateResult(self, nums, n):
        res = 0
        for num in nums:
            res += math.ceil(num / n)
        return res