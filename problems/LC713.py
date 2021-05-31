# O(n)
# n = len(nums)


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        windowStart = 0
        windowProduct = nums[0]
        res = 1 if windowProduct < k else 0
        for i in range(1, len(nums)):
            windowProduct *= nums[i]
            while windowProduct >= k and windowStart <= i:
                windowProduct /= nums[windowStart]
                windowStart += 1
            if windowStart <= i:
                res += 1 + i - windowStart
        return res