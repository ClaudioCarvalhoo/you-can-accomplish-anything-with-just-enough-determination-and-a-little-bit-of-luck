# O(n)
# n = len(nums)


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixModSum = 0
        prev = 0
        seen = set()
        for i in range(len(nums)):
            prefixModSum = (prefixModSum + nums[i]) % k
            if prefixModSum in seen:
                return True
            seen.add(prev)
            prev = prefixModSum
        return False
