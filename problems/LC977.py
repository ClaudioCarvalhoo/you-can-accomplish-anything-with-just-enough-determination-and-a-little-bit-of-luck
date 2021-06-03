# O(n)
# n = len(nums)

# Sol 1
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1

        res = []
        negative = i - 1
        positive = i
        while negative >= 0 or positive < len(nums):
            nextNegative = self.getValue(nums, negative)
            nextPositive = self.getValue(nums, positive)
            if abs(nextNegative) <= abs(nextPositive):
                res.append(nextNegative * nextNegative)
                negative -= 1
            else:
                res.append(nextPositive * nextPositive)
                positive += 1
        return res

    def getValue(self, nums, i):
        if i < 0 or i >= len(nums):
            return float("inf")
        return nums[i]


# Sol 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None for _ in nums]
        negative = 0
        positive = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            val = 0
            if abs(nums[negative]) > abs(nums[positive]):
                val = nums[negative]
                negative += 1
            else:
                val = nums[positive]
                positive -= 1
            res[i] = val * val
        return res