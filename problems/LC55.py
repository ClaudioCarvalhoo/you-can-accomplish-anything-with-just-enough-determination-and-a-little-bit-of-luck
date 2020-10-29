from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGood = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastGood:
                lastGood = i

        return lastGood == 0