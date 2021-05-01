# O(n)
# n = len(nums)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        breakIndex = self.findFirstDescending(nums)
        if breakIndex is None:
            self.reverseSubList(nums, 0)
            return

        swapIndex = breakIndex + 1
        for i in range(breakIndex + 2, len(nums)):
            if nums[i] > nums[breakIndex] and nums[i] <= nums[swapIndex]:
                swapIndex = i

        self.swap(nums, breakIndex, swapIndex)
        self.reverseSubList(nums, breakIndex + 1)

    def findFirstDescending(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                return i
        return None

    def reverseSubList(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]