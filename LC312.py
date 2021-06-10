# O(n³)
# n = len(nums)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 3 and self.isAllEqual(nums):
            num = nums[0]
            return ((len(nums) - 2) * (num ** 3)) + (num ** 2) + num
        return self.chooseBestToPopLast(nums, -1, len(nums), {})

    def chooseBestToPopLast(self, nums, left, right, dp):
        if (left, right) in dp:
            return dp[(left, right)]
        if left >= right - 1:
            return 0

        res = 0
        for i in range(left + 1, right):
            popElemLast = (
                self.getBaloonVal(nums, left) * nums[i] * self.getBaloonVal(nums, right)
            )
            elemResult = (
                self.chooseBestToPopLast(nums, left, i, dp)
                + popElemLast
                + self.chooseBestToPopLast(nums, i, right, dp)
            )
            res = max(res, elemResult)

        dp[(left, right)] = res
        return res

    def getBaloonVal(self, nums, i):
        if i < 0 or i >= len(nums):
            return 1
        return nums[i]

    def isAllEqual(self, nums):
        num = nums[0]
        for i in range(len(nums)):
            if nums[i] != num:
                return False
        return True