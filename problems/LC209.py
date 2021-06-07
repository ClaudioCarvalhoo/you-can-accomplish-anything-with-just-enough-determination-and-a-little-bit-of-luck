# O(n)
# n = len(nums)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        windowSum = 0
        windowStart = 0
        for i in range(len(nums)):
            windowSum += nums[i]
            if windowSum >= target:
                while windowSum - nums[windowStart] >= target:
                    windowSum -= nums[windowStart]
                    windowStart += 1
                res = min(res, i - windowStart + 1)
        return res if res != float("inf") else 0
