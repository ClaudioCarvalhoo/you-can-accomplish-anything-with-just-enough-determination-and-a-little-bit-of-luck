# O(n)
# n = len(nums)

# Sol 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextNonZero = self.findNextNonZero(nums, 0)
        for i in range(len(nums)):
            if nextNonZero is None:
                break
            if nextNonZero <= i:
                nextNonZero = self.findNextNonZero(nums, i + 1)
            if nums[i] == 0:
                self.swap(nums, i, nextNonZero)
                nextNonZero = self.findNextNonZero(nums, nextNonZero + 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def findNextNonZero(self, nums, current):
        for i in range(current, len(nums)):
            if nums[i] != 0:
                return i
        return None


# Sol 2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(nums, nextNonZeroIndex, i)
                nextNonZeroIndex += 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]