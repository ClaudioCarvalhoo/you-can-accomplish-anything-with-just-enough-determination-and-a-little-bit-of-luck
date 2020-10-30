# O(n * t)
# n = len(nums) | t = target

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        return self.explore(nums, target, dp)

    def explore(self, nums, target, dp):
        if target in dp:
            return dp[target]
        total = 0
        for i in nums:
            if target - i >= 0:
                total += self.explore(nums, target - i, dp)
        dp[target] = total
        return total