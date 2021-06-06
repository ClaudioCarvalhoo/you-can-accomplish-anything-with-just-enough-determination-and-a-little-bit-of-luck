# O(n*log(n))
# n = len(nums)

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[-1]
        res = 0
        seen = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < cur:
                res += seen
                cur = nums[i]
            seen += 1
        return res
