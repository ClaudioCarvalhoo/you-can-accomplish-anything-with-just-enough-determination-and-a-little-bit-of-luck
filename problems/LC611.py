# O(n²)
# n = len(nums)


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for left in range(len(nums) - 2):
            canBuildFrom = left + 1
            for right in range(left + 2, len(nums)):
                while (
                    canBuildFrom < right
                    and nums[right] >= nums[left] + nums[canBuildFrom]
                ):
                    canBuildFrom += 1
                res += right - canBuildFrom
        return res